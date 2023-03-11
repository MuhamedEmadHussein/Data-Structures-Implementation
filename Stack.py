class Stack:

    def __init__(self, size):

        self.size = size
        self.data = [0] * (size)
        self.top = -1

    def push(self, data):

        if (self.top >= self.size - 1):
            print("Stack Overflow")

        else:
            self.top += 1
            self.data[self.top] = data

    def pop(self):

        if (self.top == -1):
            print("Stack Underflow")

        else:

            res = self.data[self.top]
            self.top -= 1
            self.data[self.top + 1] = 0
            return res

    def peek(self):

        if (self.top == -1):
            print("Stack Is Empty")

        else:
            print(self.data[self.top])


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack_LL:

    def __init__(self):

        self.size = 0
        self.top = None

    def push(self, data):

        new_node = Node(data=data)

        if self.top is None:

            self.top = new_node

        else:

            new_node.next = self.top
            self.top = new_node

        self.size += 1

    def pop(self):

        if self.top:

            data = self.top.data
            self.size -= 1

            if self.top.next is None:
                self.top = None

            else:
                self.top = self.top.next

            return data

        else:
            print("Stack Is Empty")

    def peek(self):

        if self.top:
            return self.top.data

        else:
            print("Stack Is Empty")

    def iter(self):
        current = self.top
        while current:
            val = current.data
            current = current.next
            yield val


# st = Stack(4)
# st.push('egg')
# st.push('ham')
# st.push('spam')
# st.push('Milk')
# st.peek()
# print(st.data)
# print(st.pop())
# print(st.data)

st = Stack_LL()
st.push("Muahammad")
st.push("Moo")
st.push("Sayed")
st.push("Ragab")
st.push("Ibrahim")
st.pop()
st.pop()

for val in st.iter():
    print(val)

print("Pop : ---------------")
print(st.pop())

print("--------------------")
for val in st.iter():
    print(val)


def check_brackets(expression):

    brackets_stack = Stack_LL()  # The stack class, we defined in previous section
    last = ' '

    for ch in expression:
        if ch in ('{', '[', '('):
            brackets_stack.push(ch)

        if ch in ('}', ']', ')'):
            last = brackets_stack.pop()

            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False

    if brackets_stack.size > 0:
        return False

    else:
        return True


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)
for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))
