class Node:

    def __init__(self, data=None):

        self.data = data
        # Initialize Pointer next
        self.next = None


# meaning that unless we change the value of next,
# the node is going to be an endpoint
# n1 = Node('eggs')
# n2 = Node('ham')
# n3 = Node('spam')

# n1.next = n2
# n2.next = n3

# METHOD ##1
class SinglyLinkedList:

    def __init__(self):

        self.head = None
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)

        if self.head is None:

            self.head = node

        else:

            current = self.head

            while current.next:

                current = current.next

            current.next = node

    def iter(self):

        current = self.head

        while current:

            val = current.data
            current = current.next
            yield val


ll = SinglyLinkedList()
ll.append("Muhammad")
ll.append("Ahmed")
ll.append("Sayed")
ll.append("Ibrahim")

for word in ll.iter():
    print(word)

# METHOD ##2


class SinglyLinkedList_2:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        self.size += 1

        if self.tail is None:

            self.head = node
            self.tail = node

        else:

            self.tail.next = node
            self.tail = node

    def append_at_a_location(self, data, index):

        current = self.head
        prev = self.head
        node = Node(data)
        count = 1

        while current:

            if index == 1:

                node.next = current
                self.head = node
                self.size += 1
                print(count)
                return

            elif index == count:

                node.next = current
                prev.next = node
                self.size += 1

                return

            count += 1
            prev = current
            current = current.next

        if count < index:
            print("The list has less number of elements")

    def append_befor(self, data):

        current = self.head
        Prev = self.head
        node = Node(data=data)

        while current:

            if (current.data == data):

                node.next = current
                Prev.next = node
                self.size += 1

            Prev = current
            current = current.next

    def iter(self):

        current = self.head

        while current:

            val = current.data
            current = current.next
            yield val

    def search(self, data):

        for node in self.iter():

            if data == node:
                return True

        return False

    def get_size(self):

        count = 0
        current = self.head

        while current:

            count += 1
            current = current.next

        return count

    def delete_first_node(self):

        current = self.head

        if self.head is None:
            print("NO Data Elements to Delete")

        elif current == self.head:

            self.head = current.next
            self.size -= 1

    def delete_last_node(self):

        current = self.head
        Prev = self.head

        while current:

            if current.next is None:

                Prev.next = current.next
                self.size -= 1

            Prev = current
            current = current.next

    def delete_intermediate_indx_node(self, index):

        current = self.head
        Prev = self.head
        count = 1

        while current:

            if count == index:

                if current == self.head:

                    current = current.next
                    self.size -= 1

                else:

                    Prev.next = current.next
                    self.size -= 1

            Prev = current
            current = current.next
            count += 1

    def delete_intermediate_data_node(self, data):

        current = self.head
        Prev = self.head

        while current:

            if current.data == data:

                if current == self.head:
                    current = current.next
                    self.size -= 1

                else:

                    Prev.next = current.next
                    self.size -= 1

            Prev = current
            current = current.next

    def clear(self):

        self.head = None
        self.tail = None


print("Class 2 -------------------------------- Methods ")
ll = SinglyLinkedList_2()
ll.append("Muhammad")
ll.append("Ahmed")
ll.append("Sayed")
ll.append("Ibrahim")
ll.append_at_a_location("moooo", 3)

ll.append_befor("Ahmed")

for words in ll.iter():
    print(words)

print(ll.search("Ibrahim"))
print(ll.size)

ll.delete_first_node()

print("After Deleting ---------------------------- ")

for words in ll.iter():
    print(words)

print(ll.size)

ll.delete_last_node()

print("After Deleting Last ---------------------------- ")

for words in ll.iter():
    print(words)

print(ll.size)

ll.delete_intermediate_indx_node(index=3)

print("After Deleting Last ---------------------------- ")

for words in ll.iter():
    print(words)

print(ll.size)

ll.delete_intermediate_data_node(data="Sayed")

print("After Deleting Last ---------------------------- ")

for words in ll.iter():
    print(words)

print(ll.size)

'''
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
def reverse(head):
    curr=head
    prev=None
    while curr is not None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev
def rearrangeList(head):
    temp=head
    while temp:
        temp.next = reverse(temp.next)
        temp=temp.next
    return head
'''
