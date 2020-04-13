from graph import Graph
from graphSearch import GraphSearch
import random


class Main:
    @staticmethod
    def createRandomUnweightedGraphIter(n):
        graph = Graph()
        visited = set()
        for i in range(0, n, 1):
            graph.addNode(i)

        for first in graph.allNodes:
            for second in graph.allNodes:
                temp = random.getrandbits(1)
                if temp:
                    if second in visited:
                        continue
                    else:
                        graph.addUndirectedEdge(first, second)
            visited.add(first)
        return graph

    @staticmethod
    def createLinkedList(n):
        linkedGraph = Graph()
        for num in range(n):
            linkedGraph.addNode(num)
            if num != 0:
                linkedGraph.addUndirectedEdge(num - 1, num)
        return linkedGraph

    @staticmethod
    def BFTRecLinkedList(graph):
        return graphSearch.BFTRec(graph)

    @staticmethod
    def BFTIterLinkedList(graph):
        return graphSearch.BFTIter(graph)


if __name__ == "__main__":
    main = Main()
    graphSearch = GraphSearch()
    graph1 = main.createRandomUnweightedGraphIter(10)
    graph2 = main.createLinkedList(10)
    graphRec = main.createLinkedList(100)
    graphIter = main.createLinkedList(10000)
    graph3 = main.BFTRecLinkedList(graphRec)
    graph4 = main.BFTIterLinkedList(graphIter)

    print(
        "-------------Unweighted Graph-------------" + "\n"
        "DFS-Rec: " + str(graphSearch.DFSRec(graph1, 4, 8)) + "\n"
        "DFS-Iter: " + str(graphSearch.DFSIter(graph1, 4, 8)) + "\n"
        "BFT-Rec: " + str(graphSearch.BFTRec(graph1)) + "\n"
        "BFT-Iter: " + str(graphSearch.BFTIter(graph1)) + "\n"
    )

    print(
        "---------------Linked List----------------" + "\n"
        "DFS-Rec: " + str(graphSearch.DFSRec(graph2, 4, 8)) + "\n"
        "DFS-Iter: " + str(graphSearch.DFSIter(graph2, 4, 8)) + "\n"
        "BFT-Rec: " + str(graphSearch.BFTRec(graph2)) + "\n"
        "BFT-Iter: " + str(graphSearch.BFTIter(graph2)) + "\n"
    )
    #
    # print(
    #     "----------------BFT-Rec Linked List-------------" + "\n" +
    #     str(graph3) + "\n" +
    #     "----------------BFT-Iter Linked List-------------" + "\n" +
    #     str(graph4) + "\n"
    # )
