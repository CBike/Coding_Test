def recursive_function(i):

    #100 번째 출력 햇을 떄 종료 되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출 합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')


recursive_function(1)