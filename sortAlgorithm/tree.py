class Node:
    def __init__(self, item=0) -> None:
        self.key = item  # 값
        self.left, self.right = None, None  # 자식 노드


# 들어온 값을 tree에 삽입
def insert(root, key):
    # root node가 없다면 새로 들어온 key가 root node가 된다.
    if root is None:
        root = Node(key)
        return root

    # root node의 값 보다 작으면 좌측 트리로 이동
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# 들어온 data 값들을 tree 구조로 반환
def treeInsert(data, root):
    for key in data:
        root = insert(root, key)


# root에 저장된 값들을 배열에 삽입
def inorderRec(root: Node, answer: list):
    if root is not None:
        inorderRec(root.left, answer)
        answer.append(root.key)
        inorderRec(root.right, answer)


data = [9, 0, 1, 8, 7, 2, 5, 4, 3, 6]
answer = []

root = Node()
treeInsert(data, root)
inorderRec(root, answer)
print(answer[1:])
