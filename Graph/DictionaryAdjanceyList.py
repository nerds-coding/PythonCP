class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {}

        for node in nodes:
            self.adj[node] = []

    def addEdges(self, src, dst):
        self.adj[src].append(dst)
        self.adj[dst].append(src)

    def iteratingNodes(self):
        for node, edges in self.adj.items():
            print(node, end=' ')
            for edge in edges:
                print('->', edge, end='')
            print()


g = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
g.addEdges('A', 'B')
g.addEdges('A', 'C')
g.addEdges('B', 'D')
g.addEdges('B', 'E')
g.addEdges('F', 'G')
g.addEdges('E', 'F')

g.iteratingNodes()
