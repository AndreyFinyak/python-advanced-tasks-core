class Stack:
    def __init__(self, obj):
        if not isinstance(obj, (list, set, tuple, dict,)):
            raise TypeError("Stack obj must be a list, set, tuple, or dict")
        self._stack = obj

    def __iter__(self):
        iter_obj = self._stack[::-1]
        return iter(iter_obj)


stack = Stack([1, 2, 3])
for item in stack:
    print(item)
