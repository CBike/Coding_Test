def is_prime_num(n):
    answer = []
    for n in n :
        for i in range(2, n):
            if n % i == 0:
                answer.append(False)
                break
            else: answer.append(True)
    print(answer)
    return answer



num_list = [2, 3, 4, 5, 6, 7, 8, 9]


is_prime_num(num_list)