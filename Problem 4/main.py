from random import randint, getrandbits
from directedgraph import DirectedGraph
from topSort import TopSort


class Main:
    @staticmethod
    def createRandomDAGIter(n):
        graph = DirectedGraph()
        for i in range(0, n, 1):
            graph.addNode(i)

        for node in graph.allNodes:
            graphLen = randint(0, n-node)
            nodesVisited = set()
            while graphLen != len(nodesVisited):
                temp = getrandbits(1)
                num = randint(node+1, n)
                if temp:
                    if num in nodesVisited:
                        continue
                    else:
                        graph.addDirectedEdge(num, node)
                        nodesVisited.add(num)
        return graph.allNodes


if __name__ == "__main__":
    main = Main
    DAG = main.createRandomDAGIter(1000)

    print(
        "-------------Directed Graph-------------" + "\n" +
         str(main.createRandomDAGIter(10)) + "\n" + "\n"
        "-------------Kahns Algorithm------------" + "\n" +
         str(TopSort.Kahns(DAG)) + "\n" + "\n"
        "-----------------mDFS-------------------" + "\n" +
         str(TopSort.mDFS(DAG))
    )
