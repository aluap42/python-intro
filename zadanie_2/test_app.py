import unittest
from app import (
    is_valid_email,
    calculate_area_of_rectangle,
    filter_even_numbers,
    format_date_yyyy_mm_dd,
    is_palindrome
)

class TestFunctions(unittest.TestCase):

    # 1. is_valid_email - sprawdza poprawność adresu e-mail
    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@example.com"))
    
    def test_invalid_email_no_at(self):
        self.assertFalse(is_valid_email("userexample.com"))
    
    def test_invalid_email_empty(self):
        self.assertFalse(is_valid_email(""))

    # 2. calculate_area_of_rectangle - zwraca pole prostokąta
    def test_area_normal(self):
        self.assertEqual(calculate_area_of_rectangle(3, 4), 12)
    
    def test_area_zero(self):
        self.assertEqual(calculate_area_of_rectangle(0, 10), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_area_of_rectangle(-3, 4)

    # 3. filter_even_numbers - zwraca tylko liczby parzyste
    def test_even_numbers_basic(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
    
    def test_even_numbers_all_even(self):
        self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6])
    
    def test_even_numbers_empty(self):
        self.assertEqual(filter_even_numbers([]), [])

    # 4. format_date_yyyy_mm_dd - konwertuje datę z "dd.mm.yyyy" do "yyyy-mm-dd"
    def test_format_date_valid(self):
        self.assertEqual(format_date_yyyy_mm_dd("01.01.2024"), "2024-01-01")
    
    def test_format_date_invalid(self):
        with self.assertRaises(ValueError):
            format_date_yyyy_mm_dd("2024/01/01")
    
    def test_format_date_empty(self):
        with self.assertRaises(ValueError):
            format_date_yyyy_mm_dd("")

    # 5. is_palindrome - sprawdza, czy tekst jest palindromem
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("kajak"))
    
    def test_palindrome_mixed_case(self):
        self.assertTrue(is_palindrome("Kajak"))
    
    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("python"))


if __name__ == "__main__":
    unittest.main()
