class TopSort:
    @staticmethod
    def Kahns(graph):
        count = 0
        queue = []
        topOrder = []
        in_degree = {node: 0 for node in graph}

        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1

        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            topOrder.append(u)
            for i in graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            count += 1

        # checking for a cycle in the graph
        if count != len(in_degree):
            return None
        else:
            return topOrder

    @staticmethod
    def mDFS(graph):
        stack = []
        nodesVisited = set()
        for node in graph:
            if node in nodesVisited:
                continue
            else:
                TopSort.mDFSUtil(graph, node, nodesVisited, stack)
        return stack

    @staticmethod
    def mDFSUtil(graph, node, nodesVisited, stack):
        nodesVisited.add(node)
        for nextNode in graph[node]:
            if nextNode in nodesVisited:
                continue
            else:
                TopSort.mDFSUtil(graph, nextNode, nodesVisited, stack)
        stack.append(node)
