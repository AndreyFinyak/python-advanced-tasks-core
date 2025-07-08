class Iterator:
    def __init__(self, *args: int):
        if not args:
            def gen():
                k = 1
                while True:
                    yield k
                    k += 1
            self.iterator = gen()
        else:
            self.iterator = iter(range(*args))

    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            num = next(self.iterator)
            if self.is_prime(num):
                return num
