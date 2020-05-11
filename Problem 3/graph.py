class Graph:
    def __init__(self):
        self.allNodes = {}

    def addNode(self, nodeVal):
        self.allNodes[nodeVal] = []

    def addUndirectedEdge(self, first, second):
        if second not in self.allNodes[first]:
            self.allNodes[first].append(second)
        if first not in self.allNodes[second]:
            self.allNodes[second].append(first)

    def removeUndirectedEdge(self, first, second):
        if second not in self.allNodes[first]:
            self.allNodes[first].remove(second)
        if first not in self.allNodes[first]:
            self.allNodes[second].remove(first)

    def getAllNodes(self):
        return set(self.allNodes)
