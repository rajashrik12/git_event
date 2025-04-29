# Kruskal's Algorithm
# Add the lowest weight edges without forming a cycle.

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, xroot, yroot):
    # Attach smaller tree under larger tree
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    result = []           # Store MST
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])  # Sort edges by weight
    parent = {}
    rank = {}

    vertices = set()
    for u, v, w in graph:
        vertices.add(u)
        vertices.add(v)

    for node in vertices:
        parent[node] = node
        rank[node] = 0

    while e < len(vertices) - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4)
]

print("\nKruskal's MST:")
print(kruskal(edges))
