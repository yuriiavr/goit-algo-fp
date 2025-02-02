class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Функція реверсування однозв'язного списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція сортування злиттям
def merge_sort_list(head):
    if not head or not head.next:
        return head
    
    # Функція для знаходження середини списку
    def get_middle(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    middle = get_middle(head)
    right_head = middle.next
    middle.next = None
    
    left_sorted = merge_sort_list(head)
    right_sorted = merge_sort_list(right_head)
    
    return merge_sorted_lists(left_sorted, right_sorted)

# Функція об'єднання двох відсортованих списків
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Перевірка
if __name__ == "__main__":
    # Створення тестового списку
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print("Початковий список:")
    print_list(head)

    # Перевірка реверсування
    reversed_head = reverse_list(head)
    print("Список після реверсування:")
    print_list(reversed_head)

    # Перевірка сортування
    sorted_head = merge_sort_list(reversed_head)
    print("Список після сортування:")
    print_list(sorted_head)

    # Перевірка об'єднання списків
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_head = merge_sorted_lists(list1, list2)
    print("Об'єднаний список:")
    print_list(merged_head)
