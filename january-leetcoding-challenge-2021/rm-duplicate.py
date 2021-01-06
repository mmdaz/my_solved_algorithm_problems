# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = None
        temp = head
        arr = []
        eq = False
        while temp is not None:
            if temp.next is None:
                if not eq:
                    arr.append(temp.val)
                temp = temp.next
                continue
            if temp.val == temp.next.val:
                eq = True
                temp = temp.next
                continue
            if eq:
               if temp.val != temp.next.val:
                   eq = False 
               temp = temp.next
               continue 
            if temp.val != temp.next.val:
                eq = False
                arr.append(temp.val)
                temp = temp.next
                continue

        # print(arr)
        head_res = None
        if arr:
            res = ListNode(arr[0])
            head_res = res

            for r in arr[1:]:
                res.next = ListNode(r)
                res = res.next
        
        return head_res


if __name__ == "__main__":
    l = [1,2,3,3,4,4,5]
    head = ListNode(val=l[0])
    head_list = head
    for i in l[1:]:
        head.next = ListNode(i)
        head = head.next
    
    s = Solution()
    res = s.deleteDuplicates(head=head_list)

    while res is not None:
        print(res.val)
        res = res.next