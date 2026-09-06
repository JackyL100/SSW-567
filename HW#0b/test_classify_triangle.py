import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertIsNone(classify_triangle(1,1,0))
        self.assertIsNone(classify_triangle(-1, 1, 0))
        self.assertIsNotNone(classify_triangle(3,4,5))

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1,1,1), "Equilateral")
        self.assertNotEqual(classify_triangle(1,2,1), "Equilateral")

    def test_right(self):
        self.assertEqual(classify_triangle(3,4,5), "Right")
        self.assertNotEqual(classify_triangle(5,12,14), "Right")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2,2,1), "Isosceles")
        self.assertNotEqual(classify_triangle(1,2,3), "Iscosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(1,2,3), "Scalene")
        self.assertNotEqual(classify_triangle(3,3,3), "Scalene")

if __name__ == '__main__':
    unittest.main()