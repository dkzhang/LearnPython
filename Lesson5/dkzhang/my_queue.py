from Lesson5.dkzhang.my_stack import MyStack


class MyQueue:
    def __init__(self):
        self.front_stack = MyStack()
        self.back_stack = MyStack()

    def push(self, v):
        self.back_stack.push(v)

    def pop(self):
        if self.length() <= 0:
            raise Exception("The queue is already empty!")

        if self.front_stack.length() <= 0:
            # move all data from back_stack to front_stack
            bLen = self.back_stack.length()
            for _ in range(bLen):
                self.front_stack.push(self.back_stack.pop())

        return self.front_stack.pop()

    def length(self):
        return self.front_stack.length() + self.back_stack.length()
