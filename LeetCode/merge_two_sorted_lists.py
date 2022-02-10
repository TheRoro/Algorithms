def mergeTwoLists(self, list1, list2):
    root = None

    if not list1:
        return list2

    if not list2:
        return list1

    if list1.val > list2.val:
        list1, list2 = list2, list1

    root = list1
    head = root

    list1 = list1.next

    # O(n + m)
    while list1 or list2:
        if list1 and list2:
            if list1.val <= list2.val:
                root.next = list1
                list1 = list1.next
            else:
                root.next = list2
                list2 = list2.next

        elif not list1:
            if list2:
                root.next = list2
                list2 = list2.next

        elif not list2:
            if list1:
                root.next = list1
                list1 = list1.next

        root = root.next

    return head
