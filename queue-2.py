from collections import deque

q= deque()
q.append(10)
q.append(20)
q.append(30)

q.popleft()

for item in q:
    print(item)