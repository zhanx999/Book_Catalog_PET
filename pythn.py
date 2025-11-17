# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        total = list1+list2
        total = sorted(total)
        return total
    
s = Solution()
l1 = [1,2,4]
l2 = [1,3,4]
print(s.mergeTwoLists(l1,l2))
        