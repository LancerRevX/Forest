import pickle

from node import Node

with open('data', 'rb') as file:
    tree = pickle.load(file)

current = tree

while 1:
    current.print()
    
    args = input('$ ')
    cmd = args[0]
    args = args[1:].split()

    try:
        path = [int(i) for i in args]
        node = current
        for i in path:
            node = node.get(i)
    except(ValueError, IndexError):
        print('Invalid path')
        continue
                
    if cmd in ('u', 'г'):
        current = node
    elif cmd == 'b':
        current = current.get(-1)
    elif cmd == 's':
        current = tree
    elif cmd in ('r', 'к'):
        node.name = input('New name: ')
    elif cmd == 'd':
        if node == current:
            current = tree
        node.delete()
    elif cmd == 'a':
        name = input('Name: ')
        node.add(Node(name))
    elif cmd == 'm':
        args = input('Where: ').split()
        try:
            path = [int(i) for i in args]
            parent = current
            for i in path:
                parent = parent.get(i)
        except(ValueError, IndexError):
            print('Invalid path')
            continue
        parent.add(node)
    elif cmd == 'h':
        print('h - help')
        print('u path - use node')
        print('b - back')
        print('s - return to root')
        print('r path - rename node')
        print('d path - delete node')
        print('a path - add new child to node')
        print('m path - move node')
        print('q - quit')
    elif cmd == 'q':
        print('Good bye!')
        break
    else:
        print('Unknown command')

with open('data', 'wb') as file:
    pickle.dump(tree, file)
