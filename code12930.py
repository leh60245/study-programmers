def solution(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == " ":
            continue
        if i % 2 == 0:
            s[i] = s[i] if s[i].isupper() else s[i].upper()
        else:
            s[i] = s[i].lower if s[i].isupper() else s[i]
        
    return ''.join(s)

print(solution("try hello world"))