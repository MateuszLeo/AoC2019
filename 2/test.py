import unittest

from .solution import part_1


class Test(unittest.TestCase):
    def test_part_1(self):
        result = part_1([1, 0, 0, 0, 99])
        assert result == [2, 0, 0, 0, 99], result
        result = part_1([2, 3, 0, 3, 99])
        assert result == [2, 3, 0, 6, 99]
        result = part_1([2, 4, 4, 5, 99, 0])
        assert result == [2, 4, 4, 5, 99, 9801]
        result = part_1([1, 1, 1, 4, 99, 5, 6, 0, 99])
        assert result == [30, 1, 1, 4, 2, 5, 6, 0, 99]


if __name__ == "__main__":
    unittest.main()
