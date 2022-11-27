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