class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def tenary_to_binary_tree(tenary):
    stack = []
    for t in reversed(tenary):
        stack.append(t)
        if stack[-2:-1] == ['?']:
            root = TreeNode(stack[-1])
            root.left = TreeNode(stack[-3]) if isinstance(stack[-3],str) else stack[-3]
            root.right = TreeNode(stack[-5]) if isinstance(stack[-5],str) else stack[-5]
            stack[-5:] = [root]
    return stack[-1]

a = tenary_to_binary_tree('5?3?2:1?2:7:9')
q = [a]

while q:
    n = q.pop(0)
    if n:
        print(n.val)
        q.append(n.left)
        q.append(n.right)


