import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(extend.add(2, -10), -8)
    def test_add_float(self):
        self.assertEqual(extend.add(2.5, 10.4), 12.9)
    def test_add_negative_float(self):
        self.assertEqual(extend.add(2.5, -5.1), -2.6)
    def test_add_zero(self):
        self.assertEqual(extend.add(11, 0), 11)
    def test_add_string(self):
        self.assertFalse(extend.add('four',5))
    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)
    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)
    def test_max_of_three_equal(self):
        self.assertFalse(extend.max_of_three(3, 3, 5))
    def test_max_of_three_string(self):
        self.assertFalse(extend.max_of_three('five', 3, 5))
    def test_max_of_three_secound(self):
        self.assertEqual(extend.max_of_three(3, 8, 5), 8)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)
    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)
    def test_median_four_outputfloat(self):
        self.assertEqual(extend.median([7,4,3,5]), 4.5)
    def test_median_string(self):
        self.assertEqual(extend.median([7, 4, 'four', 5]), 5)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()
