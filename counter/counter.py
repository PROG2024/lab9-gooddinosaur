"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    """A singleton counter class"""
    _instance = None

    def __str__(self):
        """Return current count."""
        return f"{self.__count}"

    @property
    def count(self):
        """Return current count."""
        return self.__count

    def __new__(cls):
        """Create new instance if none exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__count = 0
        return cls._instance

    def increment(self):
        """Add 1 to current count"""
        self.__count += 1
        return self.__count
