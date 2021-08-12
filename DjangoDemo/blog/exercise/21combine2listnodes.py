class List2Node(object):
    def __init__(self, item):
        self.value = item
        self.next = None


class Solution(object):
    def combine_2_listnodes(self, l1, l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        dummy = cur = List2Node(0)
        while l1 and l2:
            if l1.value < l2.value:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == '__main__':
    l1 = ll1 = List2Node(1)
    ll1.next = List2Node(2)
    ll1 = ll1.next
    ll1.next = List2Node(4)
    l2 = ll2 = List2Node(1)
    ll2.next = List2Node(3)
    ll2 = ll2.next
    ll2.next = List2Node(4)
    result = Solution().combine_2_listnodes(l1, l2)
    while result:
        print(result.value)
        result = result.next

