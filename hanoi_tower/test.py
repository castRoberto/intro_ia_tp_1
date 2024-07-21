from collections import deque


frontier = deque([1, 2, 3, 4])

frontier.extend(([5, 6]))

print(frontier)