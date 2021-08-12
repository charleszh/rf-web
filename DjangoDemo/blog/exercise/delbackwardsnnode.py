class List2Node(object):
    def __init__(self):
        self.head = None

    def add_node(self, item):
        temp = List2Node()
        temp.value = item
        temp.next = self.head
        self.head = temp

    def print_node(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

class Solution(object):
    def del_backwards_n_node(self, head, n):
        """

        :param head: 链表； n: 倒数第n个节点
        :return: 处理后的链表
        """
        A = B = head
        while n > 0:
            B = B.next
            n -= 1
        if not B:
            return head.next
        B = B.next
        while B:
            B = B.next
            A = A.next
        A.next = A.next.next
        return head

if __name__ == '__main__':
    node_list = List2Node()
    node_list.add_node(1)
    node_list.add_node(2)
    node_list.add_node(3)
    node_list.add_node(4)
    node_list.add_node(5)
    node_list.print_node()
    exa = Solution().del_backwards_n_node(node_list.head, 2)
    while exa:
        print(exa.value)
        exa = exa.next

