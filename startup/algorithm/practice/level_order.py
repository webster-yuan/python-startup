from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = [root]
    res = []

    while queue:
        level_size = len(queue)
        level_node = []

        for _ in range(level_size):
            node = queue.pop(0) # 队列头弹出
            level_node.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        res.append(level_node)
    
    return res

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(levelOrder(root))  # [[3],[9,20],[15,7]]