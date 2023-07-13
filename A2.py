import heapq

class Node:
    def __init__(self, room, cost, estimate):
        self.room = room
        self.cost = cost
        self.estimate = estimate

    def __lt__(self, other):
        if self.cost + self.estimate == other.cost + other.estimate:
            # 当估计距离相等时，按照节点编号升序排序
            return self.room < other.room
        else:
            return self.cost + self.estimate < other.cost + other.estimate

def a_star(N, M, K, edges):
    # 邻接表表示图
    graph = [[] for _ in range(N+1)]
    for x, y, d in edges:
        graph[x].append((y, d))

    # 启发式函数
    def heuristic(room):
        # 如果节点没有出边，估计距离设为0
        if not graph[room]:
            return 0
        else:
            # 否则使用每条边的权重作为估计距离
            return min(edge[1] for edge in graph[room])

    # A*算法
    k_shortest_paths = []
    start = Node(1, 0, heuristic(1))
    open_set = [start]
    while open_set and len(k_shortest_paths) < K:
        visited = set()
        current = heapq.heappop(open_set)
        if current.room == N:
            k_shortest_paths.append(current.cost)
        for neighbor, cost in graph[current.room]:
            if neighbor in visited:
                continue
            next_node = Node(neighbor, current.cost + cost, heuristic(neighbor))
            heapq.heappush(open_set, next_node)
        visited.add(current.room)

    # 补充不足K条路径的情况
    while len(k_shortest_paths) < K:
        k_shortest_paths.append(-1)

    return k_shortest_paths

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    result = a_star(N, M, K, edges)
    for path_length in result:
        print(path_length)