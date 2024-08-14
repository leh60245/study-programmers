def radixChage(n, radix):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, digith = divmod(n, radix)
        nums.append(str(digith))
    return "".join(reversed(nums))

def solution(s):
    answer = [0,0]
    while s != "1":
        c = len("".join([i if i != "0" else "" for i in s]))
        answer[1] += len(s) - c
        s = radixChage(c, 2)
        answer[0] += 1
    return answer

print(solution("110010101001"))
    
print(solution("01110"))

print(solution("1111111"))