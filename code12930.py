def solution(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == " ":
            cnt = 0
            continue
        if cnt % 2 == 0:
            s[i] = s[i] if s[i].isupper() else s[i].upper()
        else:
            s[i] = s[i].lower if s[i].isupper() else s[i]
        cnt += 1
        
    return ''.join(s)

print(solution("try hello worlds"))
print(solution("give me a cup of water"))
