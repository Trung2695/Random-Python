import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
def is_prime(n):
    import math
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.floor(math.sqrt(n)))):
        if n % i != 0:
            continue
        else:
            return False
        return True