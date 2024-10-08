def radixChage(num, radix):
    if num == 0:
        return "0"
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return "".join(reversed(nums))


def solution(n):
    return int(radixChage(n, 3)[::-1], 3)
