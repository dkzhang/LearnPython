from Lesson5.dkzhang.my_queue import MyQueue
from Lesson5.dkzhang.mystack import MyStack


class MyAdvancedQueue(MyQueue):
    # def __init__(self):
    #     super().__init__()

    def to_string(self):
        str_result = "[ "
        for i in range(1, self.length() + 1):
            v = self.pop()
            str_result += '{:>5s}, '.format(str(v))
            # str_result += str(v) + ", "
            # super().push(v)
            super().push(v)
            if i % 10 == 0:
                str_result += "\r\n  "
        str_result += '{:>5s}, '.format("]")
        return str_result

    def reverse(self):
        s_len = self.length()
        st = MyStack()
        for _ in range(s_len):
            st.push(self.pop())

        for _ in range(s_len):
            super().push(st.pop())

    def push(self, v):
        super().push(v)
        super().push(v)
