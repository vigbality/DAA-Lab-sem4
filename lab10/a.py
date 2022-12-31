
def doBFS(s, t, parent):
  visited = [False]*len(graph)
  queue = []
  queue.append(s)
  visited[s] = True
  while queue:
    u = queue.pop(0)
    for ind, val in enumerate(graph[u]):
    	if visited[ind] == False and val > 0:
    		queue.append(ind)
    		visited[ind] = True
    		parent[ind] = u
    		if ind == t:
    			return True
  return False


def ffAlgo(graph, source, sink):
  parent = [-1]*len(graph)
  max_flow = 0
  while doBFS(source, sink, parent) :
    path_flow = float("Inf")
    s = sink
    while(s != source):
      path_flow = min (path_flow,graph[parent[s]][s])
      s = parent[s]
    max_flow += path_flow
    v = sink
    while(v !=  source):
      u = parent[v]
      graph[u][v] -= path_flow
      graph[v][u] += path_flow
      v = parent[v]
  return max_flow

graph = [[0, 16, 13, 0, 0, 0],
[0, 0, 10, 12, 0, 0],
[0, 4, 0, 0, 14, 0],
[0, 0, 9, 0, 0, 20],
[0, 0, 0, 7, 0, 4],
[0, 0, 0, 0, 0, 0]]

source = 0; sink = 5

for row in graph:
  print(row)
print("\n\nThe maximum possible flow is ", ffAlgo(graph,source, sink))

