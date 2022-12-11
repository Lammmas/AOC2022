from __future__ import annotations
from in7 import *

inarr = text.splitlines()

class Node:
    def __init__(self, name: str, owner: Node = None, size: int = 0):
        self.children = set()
        self.name = name
        self.owner = None
        self.size = size

        if owner:
            self.set_parent(owner)
    
    def __repr__(self):
        print(self.children)
        return str(self.size) + " " + self.name

    def get_parent(self):
        return self.owner

    def set_parent(self, parent: Node):
        if self.owner:
            self.owner.remove_child(self)
        self.owner = parent
        self.owner.children.add(self)

    def siblings(self):
        if self.owner is None:
            return []
        return [_ for _ in self.owner.children if _ is not self]

    def get_sibling(self, name: str):
        assert self.owner, "root node can't have siblings"
        return next((x for x in self.owner.children if x.name == name), None)

    def add_sibling(self, node: Node):
        assert self.owner, "root node can't have siblings"
        self.owner.add_child(node)

    def get_child(self, name: str):
        return next((x for x in self.children if x.name == name), None)

    def add_child(self, node: Node):
        self.children.add(node)
        node.set_parent(self)
    
    def remove_child(self, node: Node):
        self.children.remove(node)
        node.set_parent(None)
    
    def add_size(self, size: int):
        self.size += size

        if self.owner is not None:
            self.owner.add_size(size)
    
    parent = property(get_parent, set_parent)
    child = property(get_child, add_child, remove_child)
    sibling = property(get_sibling, add_sibling)

# Part 1
# Find dirs of size <= 100 000; find sum of all those dirs
files = Node("/")
loc = files
it = 0

for line in inarr:
    parts = line.split()
    it += 1

    # Ugly if tree, I know, but this is for logical thinging / readability
    if parts[0] == "$" and parts[1] == "cd":
        # We're navigating
        if parts[2] == "/":
            loc = files
        elif parts[2] == "..":
            loc = loc.parent
        else:
            # We're going into a folder
            folder = Node(parts[2], loc)
            loc = folder
    elif parts[0].isdigit():
        # We're listing a file, so just add it to the tree and propagate the size up
        file = Node(parts[1], loc)
        file.add_size(int(parts[0]))

def sumSmolKids(tree: Node, sum = 0):
    if len(tree.children) > 0:
        # Only sum up folders
        if tree.size <= 100000:
            sum += tree.size

        # Add on the child folders
        for child in tree.children:
            sum += sumSmolKids(child, 0)
    
    return sum

answer1 = sumSmolKids(files)

# Part 2
# Size available: 70 000 000; Space needed: 30 000 000; Max used: 40 000 000
deleteNeeded = 30000000 - (70000000 - files.size) # 8 044 502
smollest = files

def findSmollestDeletable(tree: Node, minSize: int, currentSize: int):
    smol = currentSize

    if len(tree.children) > 0:
        # Only check folders
        if tree.size >= minSize and tree.size < currentSize:
            smol = tree.size
        
        for child in tree.children:
            smol = findSmollestDeletable(child, minSize, smol)
    
    return smol

answer2 = findSmollestDeletable(files, deleteNeeded, files.size)

print(f'First: {answer1} Second: {answer2}')