class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceeded capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Can't remove beyond!")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
