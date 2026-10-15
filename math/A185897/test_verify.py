import unittest

import verify


class A185897VerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = verify.run_verification(400, 2000)

    def test_integer_recomputation_matches_bfile(self):
        self.assertEqual(self.result["mismatches"], [])

    def test_parity_indices_match_claim(self):
        self.assertEqual(self.result["symmetric_difference"], [])

    def test_mod2_identities_i_to_vi(self):
        self.assertEqual(self.result["identities"], {key: True for key in "i ii iii iv v vi".split()})

    def test_mod2_recursion_has_one_solution_bit_at_each_index(self):
        self.assertTrue(self.result["uniqueness_ok"])
        self.assertEqual(self.result["uniqueness_n"], 400)
        self.assertEqual(self.result["uniqueness_failures"], [])


if __name__ == "__main__":
    unittest.main()
