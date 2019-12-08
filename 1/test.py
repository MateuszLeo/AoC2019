import unittest

from .solution import part_1, part_2


class Test(unittest.TestCase):
    def test_part_1(self):
        result = part_1(12)
        assert result == 2
        result = part_1(14)
        assert result == 2

    def test_part_2(self):
        result = part_2(1969)
        assert result == 966
        result = part_2(100756)
        assert result == 50346


if __name__ == "__main__":
    unittest.main()
