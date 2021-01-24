import math

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class BellmanFord:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.weight_by_edges = {(e.u, e.v): e.weight for e in edges}
    
    def solve(self, source):
        n = len(self.vertices)
        dist = {v: math.inf for v in self.vertices}
        pred = {v: None for v in self.vertices}
        dist[source] = 0

        for i in range(n):
            changed = False
            for edge in self.edges:
                if dist[edge.u] == math.inf:
                    continue
                if dist[edge.v] > dist[edge.u] + edge.weight:
                    dist[edge.v] = dist[edge.u] + edge.weight
                    pred[edge.v] = edge.u
                    changed = True

        if changed:
            raise RuntimeError("Graph contains a negative weight cycle.")

        result = {}
        for vertex in vertices:
            if vertex == source:
                continue
            path, distance = [], 0
            curr_vertex = vertex
            while True:
                path.append(curr_vertex)
                if pred[curr_vertex] is None:
                    break
                distance += self.weight_by_edges[(pred[curr_vertex], curr_vertex)]
                curr_vertex = pred[curr_vertex]
            path = list(reversed(path))
            result[vertex] = (distance, path) if len(path) > 1 else (math.inf, [])
        return result


if __name__ == "__main__":
    vertices = set(["A", "B", "C"])
    edges = [Edge("A", "B", 2), Edge("A", "C", 1), Edge("B", "C", 1)]
    # vertices = set(["A", "B", "C", "D", "E"])
    # edges = [Edge("A", "B", 1), Edge("A", "C", 5), Edge("B", "C", 1), Edge("B", "D", 3), Edge("C", "D", 1)]
    bf = BellmanFord(vertices, edges)
    result = bf.solve("A")
    print(result)
