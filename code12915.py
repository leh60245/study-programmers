def solution(strings, n):
    # 정렬 함수에서 key 값을 변경한다.
    # key 값이 어떤 것이든 기준이 될 수 있는 형식이라면, 무엇이든지 사용할 수 있다.
    # 핵심 ==> 데이터를 어떤 관점으로 바라볼 것인지, 그리고 이를 기반으로 기준을 어떻게 명시하는가
    # 이를 유념한다면, 들어갈 key 값의 제한 사항은 "존재하지 않는다".
    # key 값으로 들어가는 데이터를 튜플로 만든다.
    # 이러면 해당 튜플순으로 정렬된다.
    return sorted(strings, key=lambda x: (x[n], x))


strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))
