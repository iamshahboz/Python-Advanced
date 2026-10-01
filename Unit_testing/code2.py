import unittest 

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 


class TestDivide(unittest.TestCase):
    def test_divide_normal_case(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10,0)

    def test_divide_by_zero_error_message(self):
        with self.assertRaises(ValueError) as context:
            divide(10,0)

        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
    
