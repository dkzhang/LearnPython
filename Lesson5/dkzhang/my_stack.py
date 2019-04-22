
class MyStack:
    def __init__(self):
        self.the_array = [0]
        self.the_index = -1
        self.the_capacity = 1

    def push(self, v):
        if self.the_index + 1 >= self.the_capacity:
            # double the capacity
            self.the_array.extend([0 for _ in range(self.the_capacity)])
            self.the_capacity *= 2

        # push the value
        self.the_array[self.the_index + 1] = v
        self.the_index += 1

    def pop(self):
        if self.the_index < 0:
            raise Exception("The stack is already empty!")
        v = self.the_array[self.the_index]
        self.the_index -= 1
        return v

    def length(self):
        return self.the_index + 1



