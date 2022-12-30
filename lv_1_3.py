"""

연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다.
두 정수 num과 total이 주어집니다.
연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
"""

def solution(num: int, total: int) -> list:
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]



sol = solution(3, 12)
print(sol)
sol = solution(5, 15)
print(sol)
sol = solution(4, 14)
print(sol)
sol = solution(5, 5)
print(sol)