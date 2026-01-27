# Tricky problems from neetcode



# Problem: Linked List cycle: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150

# tortoise and hare solution
# if there is a cycle then it stands that eventually the fast and slow will meet, the slow moves one and the fast moves two, if the distance
# between them is at most n-1 at any point then it takes O(n) to reach the slow pointer from the fast pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         tortoise = head
#         hare = head
#         while hare and hare.next:
#             tortoise = tortoise.next
#             hare = hare.next.next
#             if tortoise == hare:
#                 return True
#         return False

# ---- End -----

# Problem: Reorder Linked List: https://neetcode.io/problems/reorder-linked-list/question
# Simple reverse linked list by indices and compare afterwards solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         idx = 0
#         curr = head
#         while curr:
#             curr = curr.next
#             idx += 1
#         length = idx
#         idx = 0
#         curr = head
#         while idx <= length // 2:
#             if idx == (length //2):
#                 temp = curr.next
#                 curr.next = None
#                 curr = temp
#             else:
#                 curr = curr.next
#             idx += 1
        
#         prev = None
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev, curr = curr, temp
#         reversedHead = prev
#         newHead = head
#         while head and reversedHead:
#             h1, r1 = head.next, reversedHead.next
#             head.next = reversedHead
#             reversedHead.next = h1
#             head, reversedHead = h1, r1
        
# fast and slow node reversing solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow, fast = head,head
#         while fast and fast.next:
#             slow, fast = slow.next, fast.next.next

#         curr = slow.next
#         slow.next = None
#         prev = None
#         while curr:
#             temp = curr.next 
#             curr.next = prev
#             prev = curr
#             curr = temp
#         reversedHead = prev

#         while head and reversedHead:
#             nextH, nextR = head.next, reversedHead.next
#             head.next = reversedHead
#             reversedHead.next = nextH
#             head,reversedHead = nextH, nextR

# ---- End -----

# Problem: Maximum Depth of Binary Tree https://neetcode.io/problems/depth-of-binary-tree/question

# Solution with recursive dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         nodes = max(self.maxDepth(root.left), self.maxDepth(root.right))
#         return 1 + nodes
        
        
# iterative dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         stack = [[root, 1]]
#         res = 0

#         while stack:
#             node, depth = stack.pop()

#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
#         return res

# breadth first search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         q = deque()
#         if root:
#             q.append(root)

#         level = 0
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
#         return level

# Problem: Subtree of Another Tree: 
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and 
# node values of subRoot and false otherwise. It's tricky with conditionals on the root and subroot

# Where m is the number of nodes in subRoot and n is the number of nodes in root

# time - O(m * n) 
# space - O(m + n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         if root == None:
#             return "$#"

#         return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

#     def z_function(self, s: str) -> list:
#         z = [0] * len(s)
#         l, r, n = 0, 0, len(s)
#         for i in range(1, n):
#             if i <= r:
#                 z[i] = min(r - i + 1, z[i - l])
#             while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#                 z[i] += 1
#             if i + z[i] - 1 > r:
#                 l, r = i, i + z[i] - 1
#         return z

#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         serialized_root = self.serialize(root)
#         serialized_subRoot = self.serialize(subRoot)
#         combined = serialized_subRoot + "|" + serialized_root

#         z_values = self.z_function(combined)
#         sub_len = len(serialized_subRoot)

#         for i in range(sub_len + 1, len(combined)):
#             if z_values[i] == sub_len:
#                 return True
#         return False

# Lowest Common Ancestor in Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         curr = root

#         while curr:
#             minVal = min(p.val, q.val)
#             maxVal = max(p.val,q.val)
#             if curr.val < minVal:
#                 curr = curr.right
#             elif curr.val > maxVal:
#                 curr = curr.left
#             else:
#                 return curr

# Problem: Valid Binary Search Tree

# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (left < node.val < right):
#                 return False

#             return valid(node.left, left, node.val) and valid(
#                 node.right, node.val, right
#             )

#         return valid(root, float("-inf"), float("inf"))

# KTH smallest elemt in a BST (1-indexed)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         cnt = k
#         res = root.val

#         def dfs(node):
#             nonlocal cnt, res
#             if not node:
#                 return

#             dfs(node.left)
#             cnt -= 1
#             if cnt == 0:
#                 res = node.val
#                 return
#             dfs(node.right)

#         dfs(root)
#         return res

# Problem: Design Add and Search Word Data Structure

# tricky with for loop and recursion and wildcard

# class Node:
#     def __init__(self):
#         self.nodes = [None for i in range(26)]
#         self.isWord = False

# class WordDictionary:

#     def __init__(self):
#         self.root = Node()

#     def addWord(self, word: str) -> None:
#         curr = self.root
#         for char in word:
#             i = ord(char) - ord('a')
#             if not curr.nodes[i]:
#                 curr.nodes[i] = Node()
#             curr = curr.nodes[i]
#         curr.isWord = True

#     def search(self, word: str) -> bool:
#         curr = self.root
#         if not word:
#             return True
#         def dfs(node, idx):
#             text = word[idx:]
#             curr = node
#             for char in text:
#                 if char != '.':
#                     i = ord(char) - ord('a')
#                     if not curr.nodes[i]:
#                         return False
#                     curr = curr.nodes[i]
#                 else:
#                     for n in curr.nodes:
#                         if n != None and dfs(n,idx+1):
#                             return True
#                     return False
#                 idx += 1
#             return curr.isWord
#         return dfs(self.root, 0)

# Problem: Permutations

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 0:
#             return [[]]
        
#         perms = self.permute(nums[1:])
#         res = []
#         for perm in perms:
#             for i in range(len(perm)+1):
#                 p = perm.copy()
#                 p.insert(i, nums[0])
#                 res.append(p)
#         return res

# Problem: Task Scheduler:

# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. 
# You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     count = {}
    #     for t in tasks:
    #         count[t] = count.get(t,0) + 1
    #     tasks = [val*-1 for val in list(count.values())]
    #     heapq.heapify(tasks)
    #     queue= deque()
    #     t = 0
    #     while queue or tasks:
    #         t += 1
    #         if tasks:
    #             val = heapq.heappop(tasks) + 1
    #             if val != 0:
    #                 queue.append([val, t+n])
            
    #         if queue and queue[0][1] == t:
    #             val,_ = queue.popleft()
    #             heapq.heappush(tasks, val)
    #     return t