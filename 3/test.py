import unittest

from .solution import part_1


class Test(unittest.TestCase):
    def test_part_1(self):
        result = part_1(
            [
                "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(sep=","),
                "U62,R66,U55,R34,D71,R55,D58,R83".split(sep=","),
            ]
        )
        assert result == 159, result
        result = part_1(
            [
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(sep=","),
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(sep=","),
            ]
        )
        assert result == 135, result


if __name__ == "__main__":
    unittest.main()
