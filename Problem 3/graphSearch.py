class GraphSearch:

    def DFSRec(self, graph, start, end):
        path = []
        nodesVisited = set()
        return self.DFSUtil(graph, start, end, nodesVisited, path)

    def DFSUtil(self, graph, start, end, nodesVisited, path):
        nodesVisited.add(start)
        path.append(start)
        if start == end:
            return 1
        else:
            for node in graph.allNodes[start]:
                if node in nodesVisited:
                    continue
                else:
                    nextNode = self.DFSUtil(graph, node, end, nodesVisited, path)
                    if bool(nextNode):
                        return path
            return None

    @staticmethod
    def DFSIter(graph, start, end, nodesVisited=None):
        path = []
        if nodesVisited is None:
            nodesVisited = set()
        stack = [start]
        while len(stack):
            adjacent = stack.pop()
            path.append(adjacent)
            nodesVisited.add(adjacent)
            if adjacent == end:
                return path
            else:
                for node in reversed(graph.allNodes[adjacent]):
                    if node in nodesVisited:
                        continue
                    else:
                        stack.append(node)

    def BFTRec(self, graph):
        path = []
        nodesVisited = set()
        for node in graph.getAllNodes():
            if node in nodesVisited:
                continue
            else:
                queue = [node]
                self.BFTUtil(graph, path, queue, nodesVisited)
        return path

    def BFTUtil(self, graph, path, queue, nodesVisited):
        while len(queue):
            adjacent = queue.pop(0)
            path.append(adjacent)
            nodesVisited.add(adjacent)
            for node in graph.allNodes[adjacent]:
                if node in nodesVisited:
                    continue
                else:
                    queue.append(node)
            return self.BFTUtil(graph, path, queue, nodesVisited)

    @staticmethod
    def BFTIter(graph):
        path = []
        nodesVisited = set()
        for node in graph.allNodes:
            if node in nodesVisited:
                continue
            else:
                queue = [node]
                while len(queue) != 0:
                    adjacent = queue.pop(0)
                    path.append(adjacent)
                    nodesVisited.add(adjacent)
                    for neighbor in graph.allNodes[adjacent]:
                        if neighbor in nodesVisited:
                            continue
                        else:
                            queue.append(neighbor)
        return path
