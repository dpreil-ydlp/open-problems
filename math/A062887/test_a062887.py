import unittest
from pathlib import Path

from a062887 import a


class A062887Tests(unittest.TestCase):
    def test_first_26_terms_match_b_file(self):
        expected = [int(line.split()[1]) for line in Path(__file__).with_name("b062887.txt").read_text().splitlines()
                    if line and not line.startswith("#")]
        self.assertEqual([a(n) for n in range(26)], expected)

    def test_no_solution_terms(self):
        self.assertEqual(a(62), 0)
        self.assertEqual(a(187), 0)

    def test_58_digit_a56_is_divisible_by_113(self):
        value = a(56)
        self.assertEqual(len(str(value)), 58)
        self.assertEqual(value % 113, 0)


if __name__ == "__main__":
    unittest.main()
