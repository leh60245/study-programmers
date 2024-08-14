def solution(s):
    change, zero = 0, 0
    while s != "1":
        change += 1
        num = s.count('1')  # count() 메서드를 사용하여 1의 개수를 알아낼 수 있다.
        zero += len(s) - num    # 단순하게 길이를 빼는 것으로 알 수 있다.
        s = bin(num)[2:]
    return [change, zero]

print(solution("110010101001"))
    
print(solution("01110"))

print(solution("1111111"))