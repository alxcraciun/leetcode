# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toNode(lista: list) -> ListNode:

    if not lista:
        return

    head = ListNode(val = lista[0], next = None)
    print(head.val, end = ' ')

    if len(lista) == 1:
        return head

    aux = ListNode()
    head.next = aux

    for i in range(1, len(lista)):
        aux.val = lista[i]
        print(aux.val, end = ' ')
        aux.next = ListNode()
        aux = aux.next
    aux = None

    print()
    return head

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None and list2 == None:
            return

        head = ListNode()
        merged = head

        while list1!= None and list2 != None:
            if list1.val <= list2.val:
                merged.val = list1.val
                list1 = list1.next
            else:
                merged.val = list2.val
                list2 = list2.next

            merged.next = ListNode()
            merged = merged.next

        while list1 != None:
            merged.val = list1.val
            list1 = list1.next
            if list1 != None:
                merged.next = ListNode()
                merged = merged.next

        while list2 != None:
            merged.val = list2.val
            list2 = list2.next
            if list2 != None:
                merged.next = ListNode()
                merged = merged.next

        return head


list1 = toNode( [1,2,4] )
list2 = toNode( [1,3,4] )

solution = Solution()
print(solution.mergeTwoLists(list1, list2))