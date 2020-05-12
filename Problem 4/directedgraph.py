class DirectedGraph:
    def __init__(self):
        self.allNodes = {}

    def addNode(self, nodeVal):
        if nodeVal not in self.allNodes:
            self.allNodes[nodeVal] = []

    def addDirectedEdge(self, first, second):
        if first in self.allNodes:
            self.allNodes[first].append(second)

    def removeDirectedEdge(self, first, second):
        if first in self.allNodes:
            self.allNodes[first].remove(second)

    def getAllNodes(self):
        return set(self.allNodes.keys())
