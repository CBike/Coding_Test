
def solution(num_list):
    answer = [True] * len(num_list)
    for i in range(len(num_list)):
        num = num_list[i]
        for j in range(2, num):
            if num % j == 0:
                answer[i] = False
                break
        else: answer[i] = True
    print(answer)
    return answer



num_list = [2, 3, 4, 5, 6, 7, 8, 9]


solution(num_list)