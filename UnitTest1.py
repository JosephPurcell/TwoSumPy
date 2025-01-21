import unittest
from TwoSum import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        output = solution.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(output, [0,1])  # add assertion here

    def test_2(self):
        solution = Solution()
        output = solution.twoSum([3, 2, 4], 6)
        self.assertEqual(output, [1, 2])  # add assertion here

    def test_3(self):
        solution = Solution()
        output = solution.twoSum([3, 3], 6)
        self.assertEqual(output, [0,1])  # add assertion here

    def test_4(self):
        solution = Solution()
        output = solution.twoSum([1, 5, 9, 13, 22, 2, 7], 15)
        self.assertEqual(output, [3,5])  # add assertion here


if __name__ == '__main__':
    unittest.main()
