class Node:

    def __init__(self, info, priority):
        self.info = info
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def insert(self, node):

        if len(self.queue) == 0:
            # add the new node
            self.queue.append(node)

        else:

            for x in range(0, len(self.queue)):

                if node.priority >= self.queue[x].priority:
                    if x == (len(self.queue) - 1):
                        self.queue.insert(x + 1, node)

                    else:
                        continue

                else:
                    self.queue.insert(x, node)
                    return True

    def delete(self):
        # remove the first node from the queue
        x = self.queue.pop(0)
        print("Deleted data with the given priority-", x.info, x.priority)
        return x

    def show(self):
        for x in self.queue:
            print(str(x.info) + " - " + str(x.priority))


class PriorityQueueHeap:

    def __init__(self):
        self.queue = [()]
        self.size = 0

    def insert(self, priority, info):
        self.queue.append((priority, info))
        self.size += 1
        self.arrange(self.size)

    def arrange(self, k):

        while (k // 2) > 0:

            if self.queue[k][0] < self.queue[k//2][0]:
                self.queue[k], self.queue[k //
                                          2] = self.queue[k//2], self.queue[k]

            k //= 2

    def minChild(self, k):

        if (k * 2 + 1) > self.size:
            return k * 2

        elif self.queue[k * 2][0] < self.queue[k * 2 + 1][0]:
            return k * 2

        else:
            return k * 2 + 1

    def sink(self, k):

        while k * 2 <= self.size:

            mc = self.minChild(k)
            if self.queue[k][0] > self.queue[mc][0]:
                self.queue[k], self.queue[mc] = self.queue[mc], self.queue[k]

            k = mc

    def delete_at_root(self):
        x = self.queue[1]
        self.queue[1] = self.queue[self.size]
        self.queue.pop()
        self.size -= 1
        self.sink(1)
        return x


# p = PriorityQueue()
# p.insert(Node("Cat", 13))
# p.insert(Node("Bat", 2))
# p.insert(Node("Rat", 1))
# p.insert(Node("Ant", 26))
# p.insert(Node("Lion", 25))
# p.show()
# p.delete()

h = PriorityQueueHeap()
h.insert(2, "Bat")
h.insert(13, "Cat")
h.insert(18, "Rat")
h.insert(26, "Ant")
h.insert(3, "Lion")
h.insert(4, "Bear")
print(h.queue)

for i in range(h.size):
    n = h.delete_at_root()
    print(n)
    print(h.queue)
    
