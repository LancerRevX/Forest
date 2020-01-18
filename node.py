class Node:
    def __init__(self, name, parent = 0):
        self.name = name
        if parent == 0:
            self.parent = self
        else:
            self.parent = parent
        self.children = []

    def get(self, i):
        if i < -1:
            return self.get(i + 1)
        if i == -1:
            return self.parent
        if i == 0:
            return self
        else:
            return self.children[i - 1]

    def add(self, node):
        if node != self and not node.is_predecessor(self):
            if node.parent != node:
                node.parent.remove(node)
            node.parent = self
            self.children.append(node)

    def remove(self, node):
        if node in self.children:
            self.children.remove(node)

    def delete(self):
        if self.parent != self:
            self.parent.remove(self)

    def is_predecessor(self, node):
        if node in self.children:
            return True
        for child in self.children:
            if child.is_predecessor(node):
                return True
        return False

    def move(self, node):
        if self != node and not self.is_predecessor(node):
            self.parent = node
            print('moved')
        else:
            print('not moved')

    def print(self, i = 0, indent = ''):
        print(f'{indent}[{i}]:{self.name}')
        for i, child in enumerate(self.children):
            child.print(i + 1, indent + '    ')

