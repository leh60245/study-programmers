def solution(numbers: list):
    arr = set() # 숫자 중복을 방지하기 위한 set 지정
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            arr.add(numbers[i] + numbers[j])
    return sorted(list(arr))    # list로 변경 후 오름차순 나열

print(solution([2,1,3,4,1]))