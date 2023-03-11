class Node:

    def __init__(self, data=None, next=None, prev=None):

        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.count = 0

    def append_at_start(self, data):

        new_node = Node(data=data, next=None, prev=None)

        if self.head is None:

            self.head = new_node
            self.tail = self.head

        else:

            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    def append_at_last(self, data):

        new_node = Node(data=data, prev=None, next=None)

        if self.head is None:

            self.head = new_node
            self.tail = self.head

        else:

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def append_at_position(self, data, index):

        current = self.head
        prev = self.head
        new_node = Node(data=data, prev=None, next=None)
        count = 0

        while current:

            if index == 0:

                self.head = new_node
                self.tail = self.head
                self.count += 1
                return

            elif index == count:

                prev.next = new_node
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node
                self.count += 1
                return

            count += 1
            prev = current
            current = current.next

        if index > count:
            print("Index Out of Range")

    def append_before_val(self, data, new_val):

        current = self.head
        prev = self.head
        new_node = Node(data=new_val, prev=None, next=None)

        while current:

            if data == current.data:

                prev.next = new_node
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node
                self.count += 1
                return

            prev = current
            current = current.next

    def iter(self):

        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):

        for node_data in self.iter():

            if data == node_data:
                print(f"{data} is present in a list")
                return

        print(f"{data} is not found in a list")

    def delete(self, data):

        current = self.head
        deleted = False

        if current is None:
            print("List is Empty, No Deletion")

        elif current.data == data:
            self.head.next = None
            deleted = True
            self.head = current.next
            self.count -= 1

        elif self.tail.data == data:

            self.tail = self.tail.prev
            self.tail.next = None
            deleted = True
            self.count -= 1

        else:

            prev = self.head
            Next = self.head
            while current:

                if current.data == data:
                    # OR
                    #    current.prev.next = current.next
                    #    current.next.prev = current.prev
                    prev.next = Next
                    Next.prev = prev
                    current.next = None
                    current.prev = None
                    deleted = True
                    self.count -= 1
                    return

                prev = current
                current = current.next
                Next = current.next


dl = DoublyLinkedList()
dl.append_at_start("Muhammad")
dl.append_at_start("Muhammad")
dl.append_at_start("Muhammad")
dl.append_at_start("Muhammad")
dl.append_at_last("Moooo")
dl.append_at_start("Maged")
dl.append_at_position("Ibrahim", 3)
dl.append_before_val("Moooo", "Sayed")
dl.contains("Sayed")
dl.delete("Muhammad")
for data in dl.iter():
    print(data)
