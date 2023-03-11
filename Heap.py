class MinHeap:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def arrange(self, k):

        while k // 2 > 0:

            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k//2] = self.heap[k // 2], self.heap[k]

            else:
                break

            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    # Helper For Deletion
    # Which Child to compare with parent node

    def minChild(self, k):

        if 2 * k + 1 > self.size:
            return k * 2

        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2

        else:
            return k * 2 + 1

    def sink(self, k):

        while k * 2 <= self.size:
            mc = self.minChild(k=k)

            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]

            k = mc

    def delete_at_root(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def delete_at_location(self, location):
        item = self.heap[location]
        self.heap[location] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(location)
        return item
        
    ######## Soting From Heap 
    def heap_sort(self):
        sorted_list = []
        for _ in range(self.size):
            n = self.delete_at_root()
            sorted_list.append(n)

        return sorted_list


# h = MinHeap()
# for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
#     h.insert(i)

# print(h.heap)

# h = MinHeap()
# for i in (2, 3, 5, 7, 9, 10, 6):
#     h.insert(i)
# print(h.heap)
# n = h.delete_at_root()
# print(n)
# print(h.heap)

h = MinHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]

for i in unsorted_list:
    h.insert(i)

print("Unsorted list: {}".format(unsorted_list))
print("Sorted list: {}".format(h.heap_sort()))
