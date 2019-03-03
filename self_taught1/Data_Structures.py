# list tuples dictionaries
# stacks and queues
# putting item on stack is pushing
# add and remove from stack, only add remove last item
# removing from stack is popping
# called a LIFO data structure, last in first out

# a queue is a data structure and is FIFO
# ex line of people first person gets ticket


class Stack:
    def __init__(self):
        self.items = []  # list to store data

    def is_empty(self):
        return self.items == []  # checks if stack empty

    def push(self, item):
        self.items.append(item)  # adds items to end

    def pop(self):
        return self.items.pop()  # remove and return last item

    def peek(self):
        last = len(self.items) - 1  # returns last item not remove
        return self.items[last]

    def size(self):
        return len(self.items)  # returns number of items


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
for i in range(1, 11):
    stack.push(i)
print(stack.items)
print(stack.size())
stack.pop()
print(stack.items)
stack.push(5)
for i in range(1,10):
    stack.push(i)
print(stack.items)
print(stack.peek())

# print hello backwards
stack3 = Stack()
for c in "Thomas":
    stack3.push(c)

reversed_string = ""
for i in range(len(stack3.items)):
    reversed_string += stack3.pop()
print(reversed_string)

yester = Stack()
for c in "Yesterday":
    yester.push(c)
print(yester.items[0])
reversed_string = ""
for i in range(len(yester.items)):
    reversed_string += yester.pop()
print(reversed_string)
print()


class Queue:
    def __init__(self):  # list
        self.items = []

    def is_empty(self):  # checks if empty
        return self.items == []

    def enqueue(self, item):  # adds item to front index 0
        self.items.insert(0, item)

    def dequeue(self):  # uses pop to delete item at front of quese
        return self.items.pop()

    def size(self):  # checks list of items
        return len(self.items)

aq = Queue()
print(aq.is_empty())

for i in range(11):
    aq.enqueue(i)
print(aq.items)
print(aq.size())
aq.dequeue()
print(aq.size())
for i in range(aq.size()):
    print(i)

print()
