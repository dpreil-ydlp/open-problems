import math
import unittest

from verify import (
    admissible_numbers,
    first_multiple,
    first_multiples_through,
    geometric_sum_mod,
    is_admissible,
    x_5k_mod,
)
from verify2 import (
    factor_integer,
    first_witness_residue_scan,
    multiplicative_order_10,
    x_5k_horner_mod,
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

    def test_exact_factorization_and_order(self):
        self.assertEqual(factor_integer(360), {2: 3, 3: 2, 5: 1})
        self.assertEqual(multiplicative_order_10(7), 6)
        self.assertEqual(multiplicative_order_10(1), 1)
        for modulus in range(1, 150):
            if math.gcd(modulus, 10) == 1:
                order = multiplicative_order_10(modulus)
                if modulus != 1:
                    self.assertEqual(pow(10, order, modulus), 1)
                for proper_divisor in range(1, order):
                    if order % proper_divisor == 0:
                        self.assertNotEqual(pow(10, proper_divisor, modulus), 1)

    def test_incremental_scan_finds_smallest_in_numeric_order(self):
        self.assertEqual(first_witness_residue_scan(29, 15), (3, 9))
        self.assertEqual(first_witness_residue_scan(1, 5), (1, 1))
        self.assertIsNone(first_witness_residue_scan(125, 3000))

    def test_residue_scan_matches_brute_force_for_small_multipliers(self):
        for m in range(1, 52, 2):
            expected, length = first_multiple(m, max_len=80)
            if expected is None:
                self.assertIsNone(first_witness_residue_scan(m, 80), m)
            else:
                result = first_witness_residue_scan(m, 80)
                self.assertEqual(result[0], length, m)
                units = int(str(expected)[-1])
                self.assertEqual(result[1], units, m)

    def test_digit_horner_matches_exact_repeating_pattern(self):
        for k in range(1, 9):
            digits = [str((5 + 2 * i) % 10) for i in range(5 * k)]
            value = int("".join(reversed(digits)))
            for modulus in (1, 25, 41, 125, 1009):
                self.assertEqual(x_5k_horner_mod(k, modulus), value % modulus)


if __name__ == "__main__":
    unittest.main()
