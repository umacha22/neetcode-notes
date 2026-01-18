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
