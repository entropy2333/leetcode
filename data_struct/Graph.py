class Graph(object):
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        '''
        得到图的所有顶点
        :return:
        '''
        return list(self.gdict.keys())

    def addVertex(self, vrtx):
        '''
        添加一个顶点
        :param vrtx:
        :return:
        '''
        if vrtx not in self.gdict:
            self.gdict[vrtx] = {}

    def addEdge(self, edge):
        '''
        添加一个边
        :param edge:
        :return:
        '''
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].add(vrtx2)
        else:
            self.gdict[vrtx1] = {vrtx2, }

    def findEdge(self):
        '''
        打印所有的边
        :return:
        '''
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def dfs(self, node, visited=None):
        '''
        深度优先遍历
        :param node:
        :param visited:
        :return:
        '''
        if visited is None:
            visited = set()
        visited.add(node)
        print(node)
        for next in self.gdict[node] - visited:
            self.dfs(next, visited)
        return visited

    def bfs(self, node):
        '''
        广度优先遍历
        :param node:
        :return:
        '''
        seen = set([node])
        queue = collections.deque([node])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for next in self.gdict[vertex]:
                if next not in seen:
                    seen.add(next)
                    queue.append(next)

if __name__ == "__main__":
    graph_elements = {"a": {"b", "c"},
                    "b": {"a", "d"},
                    "c": {"a", "d"},
                    "d": {"e", },
                    "e": {"d", }
                    }
    g = Graph(graph_elements)
    print(g.getVertices())