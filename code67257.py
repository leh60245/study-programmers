from itertools import permutations
import re


def toPostFix(tokens, priority):
    stack = []  # 연산자 스택
    postfix = []  # 출력 배열(문자열)

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
            continue
        if not stack:
            stack.append(token)
            continue

        while stack:
            # 지금 token이 stack의 top에 있는 token보다 우선순위가 낮거나 같다면
            # stack에 있는 연산자를 꺼내어 출력 배열에 넣는다.
            # 이는 우선순위가 stack의 top에 있는 token보다 우선순위가 높아지거나 stack이 빌 때 까지 진행한다.
            if priority[token] <= priority[stack[-1]]:
                postfix.append(stack.pop())
                continue
            break

        stack.append(token)  # 마지막에 자신 추가

    # 모든 식을 다 돌았는데 연산자가 남아 있다면 남는 연산자를 출력 배열에 넣기
    while stack:
        postfix.append(stack.pop())

    return postfix


def calc(tokens):
    stack = []

    for token in tokens:
        # 숫자 token은 int type으로 변환 후 stack에 추가
        if token.isdigit():
            stack.append(int(token))
            continue

        num1 = stack.pop()
        num2 = stack.pop()

        if token == "*":
            stack.append(num2 * num1)
        elif token == "+":
            stack.append(num2 + num1)
        else:  # "-"
            stack.append(num2 - num1)

    return stack.pop()


def solution(expression):
    # 1. 숫자와 연산자를 분리하기
    # re.split() 함수를 사용해 '정규표현식'으로 단 한 번에 모든 숫자와 연산자 분리
    # re.split(<표현식>, <전체 문자열>): 표현식에 해당하는 문자열을 기준으로 분리
    # ex) '100*200-300' -> ['100', '*', '200', '-', '300']
    tokens = re.split(r"([-+*/()])|\s+", expression)
    operators = ["-", "+", "*"]
    answer = 0
    # 2. 순열을 사용해 연산자 3개의 우선순위를 정한다.
    # 우선순위는 set을 사용해 표시한다.
    for i in map(list, permutations(operators)):
        # {'+':0, '-':1, '*':2}
        priority = {o: p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))

    return answer

print(solution("100-200*300-500+20"))

print(solution("50*6-3*2"))