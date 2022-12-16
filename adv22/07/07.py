import re


class Node:
    def __init__(self,name):
        self.children = []
        self.name = name
        self.Size = 0

    def addChildren(self,name): # from adding dirs
        self.children.append(Node(name))

    def addChildrenNode(self,node):# adding with values
        self.children.append(node)

    def updateSize(self,Size):
        self.Size += Size




def one(data,name = 'Main'):
    tree = Node(name)
    i = 0
    while i < len(data):
        d = data[i]
        if data[i][:3] == 'dir':
            tree.addChildren(data[i][4:])
            i+=1


        elif data[i][0:4] == '$ cd':
            if data[i][-2:] == '..':
                return i,tree.Size,tree.children
            for child in tree.children:
                if child.name == data[i][5:]:
                    i+=1
                    steps,mem,children = one(data[i:],child.name)
                    i += steps + 1
                    for ch in children:
                        child.addChildrenNode(ch)
                    child.Size = mem
                    tree.Size += mem
                    break


        elif data[i][0:4] == '$ ls':
            i+=1

        else:
            size = re.findall('\d+', data[i])
            tree.updateSize(int(size[0]))
            i+=1

    if tree.name == 'Main':
        return tree
    return i, tree.Size ,tree.children


def count(tree):
    memory = 0
    max = 100000
    for child in tree.children:
        if child.children != []:
            memory += count(child)
        if child.Size <= max:
            memory += child.Size
    return memory


def small(tree,min):
    global values
    for child in tree.children:
        if child.Size >= min:
            values.append(child.Size)
            if child.children!= []:
                small(child,min=min)


if __name__ == '__main__':
    with open('in.txt') as f:
        data = f.read().splitlines()
    tree = one(data[2:])

    values = []
    min =  30000000 - (70000000 - tree.Size)
    small(tree,min)
    print(sorted(values)[0])

