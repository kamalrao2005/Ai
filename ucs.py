import heapq
def UCS(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    while priority_queue:
        cost, curr, path = heapq.heappop(priority_queue)
        if curr == goal:
            return cost, path
        if curr not in visited:
            visited.add(curr)
            for neighbor, edge_cost in graph.get(curr, []):
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + edge_cost, neighbor, path + [neighbor])
                    )
    return None, None
graph = {}
num_edges = int(input("Enter number of edges in the tree: "))
for _ in range(num_edges):
    src, dest, cost = input().split()
    cost = int(cost)
    if src not in graph:
        graph[src] = []
    graph[src].append((dest, cost))
startn = input("Enter the start node: ")
goaln = input("Enter the goal node: ")
total_cost, path = UCS(graph, startn, goaln)
if path:
    print("Goal reached")
    print("Least cost path:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("Goal not reachable")
