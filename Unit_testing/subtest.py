'''
Subtest - testing many cases without repeating yourself

'''

import unittest 

def is_even(n):
    return n % 2 == 0


# Testing without subtest

# class TestIsEven(unittest.TestCase):
#     def test_2_is_even(self):
#         self.assertTrue(is_even(2))

#     def test_3_is_odd(self):
#         self.assertFalse(is_even(3))

#     def test_0_is_even(self):
#         self.assertTrue(is_even(0))

#     def test_negative_2_is_even(self):
#         self.assertTrue(is_even(-2))


# using subtest 

class TestIsEven(unittest.TestCase):
    def test_is_even_various_inputs(self):
        test_cases = [
            (2, True),
            (3, False),
            (0, True),
            (-2, True),
            (-3, False)
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), expected)

if __name__ == "__main__":
    unittest.main()
