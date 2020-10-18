class Graph:

    def __init__(self, node):
        self.nodes = node
        self.adjList = {}

        for x in self.nodes:
            self.adjList[x] = []

    def addEdges(self, s, d):
        self.adjList[s].append(d)
        self.adjList[d].append(s)

    def iterateNodes(self):
        for node, edge in self.adjList.items():
            print(node, end=' ')
            for x in edge:
                print(' -> ', x, end='')
            print()

    def bfs(self, s):
        visited = [False]*len(self.nodes)
        q = list()

        q.append(s)
        visited[self.nodes.index(s)] = True
        while q:
            s = q.pop(0)
            print(s, end=' ')
            visited[self.nodes.index(s)] = True
            for x in self.adjList[s]:
                if(visited[self.nodes.index(x)] == False):
                    q.append(x)
                    visited[self.nodes.index(x)] = True


nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

g = Graph(nodes)
g.addEdges('A', 'B')
g.addEdges('A', 'C')
g.addEdges('B', 'D')
g.addEdges('B', 'E')
g.addEdges('E', 'F')
g.addEdges('D', 'G')
g.addEdges('F', 'A')

# g.iterateNodes()
g.bfs('A')
