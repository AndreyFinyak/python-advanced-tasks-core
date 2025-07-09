class Stack:
    def __init__(self, obj):
        if not isinstance(obj, (list, set, tuple,)):
            raise TypeError("Stack obj must be a list, set, tuple, or dict")
        self._stack = obj

    def __iter__(self):
        iter_obj = self._stack[::-1]
        return iter(iter_obj)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty stack")
        return self._stack.pop()

    def peek(self):
        if not self._stack:
            raise IndexError("peek from empty stack")
        return self._stack[-1]