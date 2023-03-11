class Node:

    def __init__(self, data=None):

        self.data = data
        # Initialize Pointer next
        self.next = None


class CircularList:

    def __init__(self):

        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):

        new_node = Node(data)

        self.size += 1

        if self.tail:

            self.tail.next = new_node

            self.tail = new_node

            new_node.next = self.head

        else:

            self.head = new_node
            self.tail = new_node
            self.tail.next = self.tail

    def delete(self, data):

        current = self.head
        prev = self.head

        while prev == current or prev != self.tail:

            if current.data == data:

                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head

                elif current == self.tail:
                    self.tail = prev
                    prev.next = self.head

                else:
                    prev.next = current.next

                self.size -= 1
                return
            prev = current
            current = current.next

    def iter(self):

        current = self.head

        while current:

            val = current.data
            current = current.next
            yield val


words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')
words.append('Muhammad')
words.append('Ahmed')
words.append('Sayed')
words.append('Ibrahim')
words.delete("Sayed")
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter >= words.size:
        break
