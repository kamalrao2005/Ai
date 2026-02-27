from collections import deque
def bfs(tree, start, goal):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print("\nBFS Traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if node == goal:
            print("\n\nGoal node found!")
            return
        for child in tree.get(node, []):
            if child not in visited:
                visited.add(child)
                queue.append(child)
    print("\n\nGoal node not found.")
tree = {}
n = int(input("Enter number of nodes: "))
print("Enter parent-child relationships:")
for _ in range(n - 1):
    parent = input("Enter parent node: ")
    child = input("Enter child node: ")

    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

    if child not in tree:
        tree[child] = []
start = input("\nEnter initial (root) node: ")
goal = input("Enter goal node: ")
bfs(tree, start, goal)
