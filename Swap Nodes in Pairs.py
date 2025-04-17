class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 新的頭部會是第二個節點
        new_head = head.next
        
        prev = None
        curr = head
        
        # 遍歷整個鏈表
        while curr and curr.next:
            # 儲存下一個節點
            next_node = curr.next
            # 交換兩個節點
            curr.next = next_node.next
            next_node.next = curr
            
            # prev 用來連接已交換的節點
            if prev:
                prev.next = next_node
                
            # 移動 prev 和 curr 指針
            prev = curr
            curr = curr.next
        
        return new_head

# 測試代碼
def print_list(node):
    while node:
        print

