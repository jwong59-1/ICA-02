from Graph import Graph


class BasicSearch:

    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        # YOUR CODE HERE
        pass


if __name__ == "__main__":
    graph = Graph()
    bs = BasicSearch(graph)
    path = bs.search("Your Cell", "Freedom")
    for node in path:
        print(node)