class WeightedGraph:
    def __init__(self):
        self.allNodes = {}

    def addNode(self, nodeVal):
        if nodeVal not in self.allNodes:
            self.allNodes[nodeVal] = {}

    def addWeightedEdge(self, first, second, edgeWeight):
        if first in self.allNodes:
            self.allNodes[first][second] = edgeWeight

    def removeDirectedEdge(self, first, second):
        if first in self.allNodes:
            self.allNodes[first].pop(second)

    def getAllNodes(self):
        return set(self.allNodes.keys())
