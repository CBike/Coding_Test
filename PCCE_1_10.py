""" 애너그램(Anagram) 이란 주어진 단어를 이루는 문자의 위치를 뒤바꾸어 새로운 단어를 만드는 것을 말합니다. 애너그램을 이용해 암호화, 복호화를 하려고합니다.

예를들어 문자열 "Hello"를 암호화  할 때, 애너그램 테이블이 [4, 2, 0, 1, 3]이면,
문자열의 0번째 값인 'H'는 애너그램 테이블의 0번째 값에 해당하는 4에 의해 4번째로 이동하고 같은 방식으로
'e'는 2번째로, 'l'은 0번째로, 'l'은 1번째로, 'o'는 3번째로 이동하여 "lleoH"가 됩니다.

위의 방법으로 만들어진 애너그램 암호문을 복호화하려면 애너그램 테이블의 인덱스와 값의 반대 방향으로 문자열의 순서를 바꿔주면 됩니다.


암호화할 문자열 text

애너그램 테이블 anagram

화를 할지 복호화를 할지가 저장된 변수 sw """


def solution(text, anagram, sw):
    answer = list(text)
    if sw:
        for n, i in enumerate(anagram):
            answer[i] = text[n]
    if not sw:
        for n, i in enumerate(anagram):
            answer[n] = text[i]

    answer = ''.join(s for s in answer)

    return answer


