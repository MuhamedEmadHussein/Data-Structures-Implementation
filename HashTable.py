class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65
        self.prime_num = 5

    def _hash(self, key):

        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1

        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size

        if self.slots[h] == None:
            self.count += 1

        self.slots[h] = item
        self.check_growth()

    def check_growth(self):
        load_factor = self.count / self.size
        if load_factor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table",
                  self.count / self.size)
            self.growth()
            print("Load factor after growing the hash table",
                  self.count / self.size)

    def growth(self):
        New_HashTable = HashTable()
        New_HashTable.size = 2 * self.size
        New_HashTable.slots = [None for i in range(New_HashTable.size)]

        for i in range(self.size):

            if self.slots[i] != None:
                New_HashTable.put(self.slots[i].key, self.slots[i].value)

            self.size = New_HashTable.size
            self.slots = New_HashTable.slots

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h+1) % self.size

        return None

    # Implementation Using Dictionary

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    # Quadratic
    def get_quadratic(self, key):

        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value

            h = (h + j*j) % self.size
            j = j + 1

        return None

    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                break

            h = (h + j*j) % self.size
            j = j+1

        if self.slots[h] == None:
            self.count += 1

        self.slots[h] = item
        self.check_growth()

    # Double Hashing
    def h2(self, key):

        mult = 1
        hv = 0

        for ch in key:
            hv += mult * ord(ch)
            mult += 1

        return hv

    def put_double_hashing(self, key, value):

        item = HashItem(key, value)
        h = self._hash(key)
        j = 1

        while self.slots[h] != None:

            if self.slots[h].key == key:
                break

            h = (h + j * (self.prime_num - (self.h2(key) %
                 self.prime_num))) % self.size
            j = j + 1

        if self.slots[h] == None:
            self.count += 1

        self.slots[h] = item
        self.check_growth()

    def get_double_hashing(self, key):

        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value

            h = (h + j * (self.prime_num - (self.h2(key) %
                 self.prime_num))) % self.size
            j = j + 1

        return None


# ht = HashTable()
# ht.put("good", "eggs")
# ht.put("better", "ham")
# ht.put("best", "spam")
# ht.put("ad", "do not")
# ht.put("ga", "collide")
# ht.put("awd", "do not")
# ht.put("add", "do not")
# ht.checkGrow()
########################################################
# ht = HashTable()
# ht.put("good", "eggs")
# ht.put("better", "ham")
# ht.put("best", "spam")
# ht.put("ad", "do not")
# ht.put("ga", "collide")
# for key in ("good", "better", "best", "worst", "ad", "ga"):
#     v = ht.get(key)
#     print(v)

##########################################################
# ht = HashTable()
# ht.put_quadratic("good", "eggs")
# ht.put_quadratic("ad", "packt")
# ht.put_quadratic("ga", "books")
# v = ht.get_quadratic("ga")
# print(v)
############################################################
# ht = HashTable()
# ht.put_doubleHashing("good", "eggs")
# ht.put_doubleHashing("better", "spam")
# ht.put_doubleHashing("best", "cool")
# ht.put_doubleHashing("ad", "donot")
# ht.put_doubleHashing("ga", "collide")
# ht.put_doubleHashing("awd", "hello")
# ht.put_doubleHashing("addition", "ok")

# for key in ("good", "better", "best", "worst", "ad", "ga"):
#     v = ht.get_doubleHashing(key)
#     print(v)

# print("The number of elements is: {}".format(ht.count))
# #######################################################

###  implementation of the hash table with separate chaining ###
class Node:

    def __init__(self, key=None, value=None):

        self.key = key
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):

        self.tail = None
        self.head = None

    def append(self, key, value):

        node = Node(key, value)

        if self.tail:
            self.tail.next = node
            self.tail = node

        else:
            self.head = node
            self.tail = node

    def traverse(self):

        current = self.head

        while current:
            print("\"", current.key, "--", current.value, "\"")
            current = current.next

    def search(self, key):

        current = self.head
        while current:
            if current.key == key:
                print("\"Record found:", current.key, "-", current.value, "\"")
                return True

            current = current.next

        return False


class HashTableChaining:

    def __init__(self):
        self.size = 6
        self.slots = [None for i in range(self.size)]

        for x in range(self.size):
            self.slots[x] = SinglyLinkedList()

    def _hash(self, key):

        mult = 1
        hv = 0

        for ch in key:
            hv += mult * ord(ch)
            mult += 1

        return hv % self.size

    def put(self, key, value):

        node = Node(key, value)
        h = self._hash(key)
        self.slots[h].append(node)

    def get(self, key):

        h = self._hash(key)
        v = self.slots[h].search(key)

    def printHashTable(self):

        print("Hash table is :- \n")
        print("Index \t\tValues\n")

        for x in range(self.size):
            print(x, end="\t\n")
            self.slots[x].traverse()

# ht = HashTableChaining()
# ht.put("good", "eggs")
# ht.put("better", "ham")
# ht.put("best", "spam")
# ht.put("ad", "do not")
# ht.put("ga", "collide")
# ht.put("awd", "do not")

# ht.printHashTable()
