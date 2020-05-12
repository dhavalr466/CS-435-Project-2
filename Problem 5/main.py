from random import randint
from heapq import heappop, heappush
from sys import maxsize
from weightedGraph import WeightedGraph


class Main:
    @staticmethod
    def createRandomCompleteWeightedGraph(n):
        graph = WeightedGraph()
        for i in range(0, n, 1):
            graph.addNode(i)

        for node in graph.allNodes:
            for num in range(0, n, 1):
                if node == num:
                    continue
                else:
                    graph.addWeightedEdge(node, num, randint(1, n ** 2))

        return graph

    @staticmethod
    def createLinkedList(n):
        linkedGraph = WeightedGraph()
        for i in range(0, n, 1):
            linkedGraph.addNode(i)
            if i == 0:
                continue
            else:
                linkedGraph.addWeightedEdge(i - 1, i, 1)
        return linkedGraph

    @staticmethod
    def findCurrent(weightLst, node):
        for weight in range(len(weightLst)):
            if weightLst[weight][1] == node:
                return weight

    @staticmethod
    def dHelper(arr, heap, visited, key):
        heappush(arr, (maxsize, key))
        heap.add(key)
        visited.add(key)
        return None

    @staticmethod
    def dijkstras(graph, start):
        dist = {}
        weightLst = []
        nodesVisited = set()
        heapVal = set()

        nodesVisited.add(start)
        weightLst.append(tuple((0, start)))
        heapVal.add(start)

        while len(weightLst) != 0:
            node_ = heappop(weightLst)
            currentNode = node_[1]
            currentWeight = node_[0]

            for key, value in graph.allNodes[currentNode].items():
                if key in nodesVisited:
                    continue

                else:
                    Main.dHelper(weightLst, heapVal, nodesVisited, key)

                if key in heapVal:
                    updateDist = currentWeight + value

                    index = Main.findCurrent(weightLst, key)

                    if updateDist > weightLst[index][0]:
                        continue

                    else:
                        weightLst[index] = (updateDist, key)

            dist[currentNode] = currentWeight
            heapVal.remove(currentNode)

        return dist


if __name__ == "__main__":
    main = Main
    graph1 = main.createRandomCompleteWeightedGraph(10)
    graph2 = main.createLinkedList(10)
    op1 = main.dijkstras(graph1, 3)
    op2 = main.dijkstras(graph2, 2)

    print(
        "-------------Complete Graph-------------" + "\n" +
        str(graph1.allNodes) + "\n" + "\n"
        "-------------Dijkstras on the graph------------" + "\n" +
        str(op1) + "\n" + "\n"
        "-------------Linked List-------------" + "\n" +
        str(graph2.allNodes) + "\n" + "\n"
        "-------------Dijkstras on the linked list------------" + "\n" +
        str(op2) + "\n"
    )
