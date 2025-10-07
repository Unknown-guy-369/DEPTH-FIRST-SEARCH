from collections import deque, defaultdict

def bfs(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True

    while queue:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if not visited[neighbour]:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path


graph = defaultdict(list)
v, e = map(int, input("Enter vertices and edges: ").split())

# Check if vertices are integers or characters
is_integer_graph = None

for _ in range(e):
    u, v = input().split()
    # Detect type on first edge
    if is_integer_graph is None:
        is_integer_graph = u.isdigit()
    # Convert to int if integer graph
    if is_integer_graph:
        u, v = int(u), int(v)
    graph[u].append(v)
    graph[v].append(u)

# Choose start automatically
if is_integer_graph:
    start = 0
else:
    start = 'A'

path = []
visited = defaultdict(bool)
traversedpath = bfs(graph, start, visited, path)
print("BFS Traversal:", traversedpath)
