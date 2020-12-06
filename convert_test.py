import unittest
import convert


class TestBinToOct(unittest.TestCase):
    def test_convert_binary_with_one_decimal(self):
        result = convert.BinToOct("011.011")
        self.assertEqual(result, "3.3")

    def test_convert_to_binary_with_one_decimal(self):
        result = convert.BinToOct("0110011")
        self.assertEqual(result, "063")


if __name__ == '__main__':
    unittest.main()
