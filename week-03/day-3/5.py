# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it
# please don`t use the built in methods
class Stack:
    def __init__(self):
        self.listofnumbers =[]
        self.remlistonnumbers = []
    def size(self):
        n = 0
        for i in self.listofnumbers:
            n += 1
        return n
    def push(self, number):
        self.listofnumbers += [number]
    def pop(self):
        self.remlistonnumbers = []
        for i in range(0, self.size()-1):
            self.remlistonnumbers += [self.listofnumbers[i]]
        self.listofnumbers = self.remlistonnumbers

kazal = Stack()
kazal.push(4)
kazal.push(5)
kazal.push(1)
kazal.push(5)
kazal.push(5
kazal.pop()
kazal.pop()



print(kazal.size())
