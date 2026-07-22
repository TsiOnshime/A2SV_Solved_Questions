# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        none_count = 0
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
            

        print(res)
        return ",".join(res)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if data[0] == "#":
            return 
        idx = 1
        root = TreeNode(int(data[0]))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            left = TreeNode(int(data[idx])) if data[idx] != "#" else None
            right = TreeNode(int(data[idx + 1])) if data[idx + 1] != "#" else None
            if left:
                node.left = left
                queue.append(left)
            if right:
                node.right = right
                queue.append(right)
            idx += 2
        return root
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna