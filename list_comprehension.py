a = [i for i in range(100)]

print(a)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i for i in range(20) if i % 2 == 0 and i != 0]
print(array)

n = 4
m = 3
array_map = [[0] * m for _ in range(n)]
print(array_map)
for item in array_map:
    print(item)


# 리스트에서 특정값을 가지는 원소를 모드 제거하기

a = [1, 2, 3, 4, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)