import sys
sys.setrecursionlimit(2000)

def find_emptyroom(chk, rooms):
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        _ = find_emptyroom(num, rooms)
    return list(rooms)

print(solution(10, [1,3,4,1,3,1]))