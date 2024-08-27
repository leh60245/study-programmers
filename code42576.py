def solution(participant, completion):
    value = 0
    answer = {}
    for part in participant:
        answer[hash(part)] = part
        value += int(hash(part))
    for comp in completion:
        value -= hash(comp)
    return answer[value]
        
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))