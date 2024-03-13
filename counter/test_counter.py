"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest


class TestCounter(unittest.TestCase):
    def test(self):
        counter1 = Counter()
        counter1.increment()
        counter1.increment()
        self.assertEqual(2, counter1.count)

        counter2 = Counter()
        self.assertEqual(counter1, counter2)
        self.assertEqual(2, counter2.count)
