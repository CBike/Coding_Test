"""
나이트는 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동하기
2. 수직으로 한 칸 이동한 뒤에 수평으로 한칸 이동하기
"""
# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1

# 나이트의 움직임의 경우의 수
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


"""
*   ord() : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
    ord('a')를 넣으면 정수 97을 반환합니다.

*   chr() : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.
    chr(97)을 하면 문자 'a'를 반환합니다.


"""