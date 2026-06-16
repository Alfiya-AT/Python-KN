class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Print Linked List
    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    # Delete First Node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        curr = self.head

        while curr.next.next:
            curr = curr.next

        curr.next = None

    # Search Element
    def search(self, key):
        curr = self.head
        position = 1

        while curr:
            if curr.data == key:
                return f"{key} found at position {position}"

            curr = curr.next
            position += 1

        return f"{key} not found"


# ---------------- DRIVER CODE ----------------

ll = LinkedList()

print("Insert at End:")
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.print_list()

print("\nInsert at Beginning:")
ll.insert_beginning(5)
ll.print_list()

print("\nDelete First Node:")
ll.delete_first()
ll.print_list()

print("\nDelete Last Node:")
ll.delete_last()
ll.print_list()

print("\nSearch Element:")
print(ll.search(20))
print(ll.search(100))