class Queue:

    def __init__(self, size):
        self.size = size
        self.data = [0] * (size)
        self.front = -1
        self.rear = -1

    def enqueue(self, data):

        if (self.rear == -1):
            self.rear += 1
            self.data[self.rear] = data
            self.front = 0

        elif (self.rear == self.size - 1):
            print("Overflow Queue")

        else:
            self.rear += 1
            self.data[self.rear] = data

    def dequeue(self):

        if (self.front == -1 or self.front >= self.size):
            print("Empty Queue")

        elif (self.front < self.size):
            res = self.data[self.front]
            self.data[self.front] = 0
            self.front += 1
            return res


# q = Queue(4)
# q.enqueue("Muahammad")
# q.enqueue("Moo")
# q.enqueue("Sayed")
# q.enqueue("Ragab")
# print("-----------------------------")
# print(q.data)
# q.enqueue("Ibrahim")

class Node(object):

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue_LL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):

        new_node = Node(data=data)

        if self.tail:

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:

            self.head = new_node
            self.tail = self.head

        self.count += 1

    def dequeue(self):

        if self.count == 1:
            data = self.head.data
            self.count -= 1
            self.head = None
            self.tail = None
            return data

        elif self.count > 1:

            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1

            return data

        else:
            print("List is Empty")
            return


# ql = Queue_LL()
# ql.enqueue(data="Muhammad")
# ql.enqueue("Mahmoud")
# ql.enqueue("Moo")
# ql.enqueue("Sayed")
# ql.enqueue("Ragab")
# print(ql.dequeue())
# print(ql.dequeue())
# print(ql.dequeue())
# print(ql.dequeue())
# print(ql.dequeue())
# ql.dequeue()
# ql.dequeue()
# ql.dequeue()
class Queue_Stack:

    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def enqueue(self, data):
        return self.Stack1.append(data)

    def dequeue(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())

        if not self.Stack2:
            print("Queue Is Empty")
            return
        return self.Stack2.pop()


ql = Queue_Stack()
ql.enqueue(data="Muhammad")
ql.enqueue("Mahmoud")
ql.enqueue("Moo")
ql.enqueue("Sayed")
ql.enqueue("Ragab")
print(ql.dequeue())
print(ql.dequeue())
print(ql.dequeue())
print(ql.dequeue())
print(ql.dequeue())
ql.dequeue()
ql.dequeue()
ql.dequeue()
