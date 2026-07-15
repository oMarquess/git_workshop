import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate("add", 2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculate("subtract", 5, 2), 3)

    # [INSTRUCTION] Teams: Add your test cases directly below this line!
    def test_modulo(self):
        self.assertEqual(calculate("modulo", 7, 3), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            calculate("modulo", 5, 0)

if __name__ == "__main__":
    unittest.main()
