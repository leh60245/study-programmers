def solution(s):
    stack = []
    for i in range(len(s)):
        if stack != [] and stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])
    return 1 if stack == [] else 0

print(solution("aabba"))