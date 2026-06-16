import json

class Task:
    def __init__(self, name, risk):
        self.name = name
        self.risk = risk

    def __repr__(self):
        return f"Task({self.name!r}, {self.risk})"


class Graph:
    """
    Adjacency dictionary representation of the jailbreak escape graph.

    Each key is a node name. Each value is a list of (neighbor_name, risk)
    """

    def __init__(self):
        self._edges = json.load(open("escape_graph.json"))

    def neighbors(self, node):
        if node not in self._edges:
            raise KeyError(f"Node '{node}' not found in graph.")
        return self._edges[node]

    def nodes(self):
        return list(self._edges.keys())

    def __contains__(self, node):
        return node in self._edges

    def __str__(self):
        lines = []
        for node, edges in self._edges.items():
            lines.append(f"{node}: {edges}")
        return "\n".join(lines)


