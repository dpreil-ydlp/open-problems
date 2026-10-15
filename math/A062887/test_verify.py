import unittest

from verify import (
    admissible_numbers,
    first_multiple,
    first_multiples_through,
    geometric_sum_mod,
    is_admissible,
    x_5k_mod,
)


class VerifyTests(unittest.TestCase):
    def test_first_admissible_values(self):
        self.assertEqual(admissible_numbers(1), [1, 3, 5, 7, 9])
        self.assertEqual(admissible_numbers(3), [197, 319, 531, 753, 975])

    def test_search_returns_minimum_in_numeric_order(self):
        self.assertEqual(first_multiple(29), (319, 3))
        self.assertEqual(first_multiple(125, max_len=10), (None, None))

    def test_shared_search_matches_per_multiplier_search(self):
        batch = first_multiples_through(25, 40)
        expected = []
        for n in range(26):
            value, length = first_multiple(2 * n + 1, 40)
            expected.append((value, length) if value is not None else None)
        self.assertEqual(batch, expected)

    def test_admissibility_rule(self):
        self.assertTrue(is_admissible(319))
        self.assertTrue(is_admissible(975))
        self.assertFalse(is_admissible(375))

    def test_geometric_sum_and_x_mod(self):
        self.assertEqual(geometric_sum_mod(100, 4, 1009), sum(pow(100, j, 1009) for j in range(4)) % 1009)
        for k in range(1, 9):
            value = int("".join(reversed([str((5 + 2 * i) % 10) for i in range(5 * k)])))
            for modulus in (3, 7, 41, 101):
                self.assertEqual(x_5k_mod(k, modulus), value % modulus)


if __name__ == "__main__":
    unittest.main()
