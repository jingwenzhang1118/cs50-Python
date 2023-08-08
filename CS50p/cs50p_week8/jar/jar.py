class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        # all the attributes need to be included in the __init__ function.
        # initialize size variable, it doesn't requre an argument in the function.
        # whenever to update the attributes, need to use underscore _size, this is the name of the variable
        # the return value does not need the underscore
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            # underscore before size is needed
            self._size += n
        else:
            raise ValueError("Exceed the capacity")

    def withdraw(self, n):
        if self.size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Not enough cookies to withdraw")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <0 or not isinstance(capacity, int):
            raise ValueError("Invalid capacity")
        else:
            self._capacity = capacity

    @property
    # does not always need setter, unless certain check needs to be done.
    def size(self):
        return self._size

