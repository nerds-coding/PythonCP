class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class AdjacencyList:

    def __init__(self, v):
        self.v = v
        self.graph = [None]*self.v

    def nodeList(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def iteratingNodes(self):
        for x in range(self.v):
            print('Vertex {0}'.format(x))
            temp = self.graph[x]
            while temp:
                print('-> {0}'.format(temp.data))
                temp = temp.next
            print()


al = AdjacencyList(7)
al.nodeList(0, 1)
al.nodeList(0, 2)
al.nodeList(0, 3)
al.nodeList(0, 4)
al.nodeList(1, 3)
al.nodeList(2, 1)


al.iteratingNodes()
