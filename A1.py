import heapq
class Puzzle:
    def __init__(self, state, goal):
        self.state = state
        self.goal = goal

    # 排序方法
    def __lt__(self, other):
        return self.priority() < other.priority()

    # 计算当前状态和目标状态之间的曼哈顿距离作为启发式函数
    def heuristic(self, current, goal):
        distance = 0
        for i in range(3): #3*3
            for j in range(3):
                current_pos = current.index(str(i * 3 + j))
                goal_pos = goal.index(str(i * 3 + j))
                current_x, current_y = current_pos // 3, current_pos % 3
                goal_x, goal_y = goal_pos // 3, goal_pos % 3
                distance += abs(current_x - goal_x) + abs(current_y - goal_y)
        return distance

    def priority(self):
        # 计算优先级
        return len(self.state_history) + self.heuristic(self.state, self.goal)

    def solved(self):
        # 判断当前状态是否为目标状态
        return self.state == self.goal

    def get_next(self):
        # 获取所有可能的下一步状态
        next_puzzles = []
        zero_pos = self.state.index('0')
        for offset in [-3, -1, 1, 3]:
            new_pos = zero_pos + offset
            if new_pos < 0 or new_pos >= 9:
                continue
            if zero_pos in [2, 5, 8] and offset == 1:
                continue
            if zero_pos in [0, 3, 6] and offset == -1:
                continue
            new_state = list(self.state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            next_puzzles.append(Puzzle(''.join(new_state), self.goal))
        return next_puzzles

    def a_star(self):
        self.state_history = [] #记录状态历史
        frontier = [self]
        while frontier:
            current = heapq.heappop(frontier)
            if current.solved():
                return len(current.state_history)
            for puzzle in current.get_next():
                if puzzle.state not in current.state_history:
                    puzzle.state_history = current.state_history + [current.state]
                    heapq.heappush(frontier, puzzle)
        return -1

if __name__ == '__main__':
    init = input().strip()
    goal = '135702684'
    # 创建puzzle对象并调用A*算法得到结果
    puzzle = Puzzle(init, goal)
    result = puzzle.a_star()
    print(result)

