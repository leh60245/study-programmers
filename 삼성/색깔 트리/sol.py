class Node:
    def __init__(self, m_id, p_id, color, max_depth) -> None:
        self.m_id = m_id
        self.p_id = p_id
        self.color = color
        self.md = max_depth
    
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, m_id, p_id, color, max_depth):
        self.root = self._insert(self.root, m_id, p_id, color, max_depth)
    
    def _insert(self, node, m_id, p_id, color, max_depth):
        if node is None:
            return Node(m_id, p_id, color, max_depth)

        