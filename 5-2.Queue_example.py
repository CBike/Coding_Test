"""
큐에 대한 이해를 돕기위한 예제
이것이 코딩테스트다 with Python 129p
"""
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)