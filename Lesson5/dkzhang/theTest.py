from Lesson5.dkzhang.my_queue import MyQueue
from Lesson5.dkzhang.my_adv_queue import MyAdvancedQueue
import random


def main():
    print('this message is from main function')

    # queue = MyQueue()
    #
    # big_num = 100
    # for i in range(big_num):
    #     r = random.randint(0, 1)
    #     if r == 1:
    #         v = random.randint(0, big_num)
    #         print("push value : ", v)
    #         queue.push(v)
    #     else:
    #         if queue.length() <= 0:
    #             print("Warning: try to pop from an empty queue!")
    #         else:
    #             v = queue.pop()
    #             print("pop value : ", v)

    q = MyAdvancedQueue()
    for i in range(35):
        q.push(i)

    print(q.length())
    print(q.to_string())
    print(q.length())
    q.reverse()
    print(q.to_string())
    print(q.length())

if __name__ == '__main__':
    main()
