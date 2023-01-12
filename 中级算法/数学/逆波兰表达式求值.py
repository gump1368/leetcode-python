#！ -*- coding: utf-8 -*-
"""
@Author: GUMP
@Create Time: 20230111
@Info：
"""


def evalRPN(tokens) -> int:
    deque = []
    for token in tokens:
        if token == '+':
            value1 = int(deque.pop())
            value2 = int(deque.pop())
            deque.append(value1 + value2)
        elif token == '-':
            value1 = int(deque.pop())
            value2 = int(deque.pop())
            deque.append(value2 - value1)
        elif token == '*':
            value1 = int(deque.pop())
            value2 = int(deque.pop())
            deque.append(value1 * value2)
        elif token == '/':
            value1 = int(deque.pop())
            value2 = int(deque.pop())
            deque.append(int(value2 / value1))
        else:
            deque.append(token)
    return deque[0]


if __name__ == '__main__':
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))