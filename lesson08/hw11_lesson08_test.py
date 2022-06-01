import unittest
from functools import reduce
import hw11_lesson08_func as func


class FuncUnittestTestCase(unittest.TestCase):

    # for is_even
    def test_zero(self):
        self.assertTrue(func.is_even(0), "0 should be even")

    def test_eleven(self):
        self.assertFalse(func.is_even(11), "11 shouldn't be even")

    def test_exception(self):
        with self.assertRaises(TypeError):
            func.is_even(True)

    # for is_odd
    def test_big_odd_num(self):
        self.assertTrue(func.is_odd(1234567891), "1234567890 should be odd")

    def test_even_num(self):
        self.assertFalse(func.is_odd(23450), "23450 shouldn't be odd")

    def test_exception_not_raised(self):
        self.assertTrue(func.is_odd("345"), "String is successfully converted into int and checked")

    # for custom_max
    def test_check_returning_max_first_num_less(self):
        self.assertEqual(func.custom_max(22, 46), max(22, 46), "Maximum out of 22, 46 is not 46")

    def test_check_returning_max_second_num_less(self):
        self.assertEqual(func.custom_max(99, 2), max(99, 2), "Maximum out of 99, 2 is not 99")

    def test_one_num_is_str(self):
        self.assertEqual(func.custom_max(8, "2"), max(8, 2), "Method did not succeed in calculating max number when "
                                                             "one of parameters os str")

    # for multiply
    def test_check_5_numbers(self):
        self.assertEqual(func.multiply(*list(range(1, 5))), reduce(lambda x, y: x*y, list(range(1, 5))),
                         "Multiplying numbers from 1 to 5 ne 24")

    def test_check_negative_num(self):
        self.assertEqual(func.multiply(-2, -4, -5), (-2 * -4 * -5),
                         f"Multiplying negative numbers gives incorrect result, should be {-2 * -4 * -5}")

    def test_negative_base(self):
        self.assertEqual(func.multiply(*list(range(1, 5)), base=-5), reduce(lambda x, y: x * y, list(range(1, 5))) * -5,
                         "Multiplying using base -5 gives incorrect result")

    # for custom_reverse
    def test_reverse_one_sign(self):
        self.assertEqual(func.custom_reverse("."), ".", "String containing a single stop sign is not reversed "
                                                        "correctly")

    def test_reverse_string(self):
        self.assertEqual(func.custom_reverse("asdfghjkl"), "lkjhgfdsa", """The string 'asdfghjkl' is not reversed 
                                                                        correctly""")

    def test_str_with_spaces(self):
        self.assertEqual(func.custom_reverse(" abcde  "), "  edcba ", """The string ' abcde  ' is not reversed 
                                                                    correctly""")

    # for upper_count
    def test_single_character(self):
        self.assertEqual(func.upper_count(","), 0, "Upper count of -> , should be 0")

    def test_string_with_several_upper_characters(self):
        self.assertEqual(func.upper_count("RGTTDSF03943cbiuaskjf"), 7, "Quantity pf upper characters should be 7")

    def test_upper_character_surrounded_special_characters(self):
        self.assertEqual(func.upper_count("*&^%$@%R)(*&@#"), 1, "Quantity of upper characters should be 1")

    # for unique
    def test_unique_positive_case(self):
        self.assertEqual(func.unique([1, 485, 3, 3, 4, 4, 5, 5]), [1, 3, 4, 5, 485], "List with unique values should "
                                                                                     "be [1, 3, 4, 5, 485]")

    def test_empty_lst(self):
        self.assertEqual(func.unique([]), [], "List with unique values should be []")

    def test_int_and_bool_unique(self):
        self.assertEqual(func.unique([3, True, 3, True, False]), [False, True, 3], "List with unique values should "
                                                                                   "be [False, True, 3]")

    # for is_pangram
    def test_is_pangram(self):
        self.assertTrue(func.is_pangram("The five boxing wizards jump quickly"), '"The five boxing wizards jump '
                                                                                 'quickly" is pangram')

    def test_is_not_pangram(self):
        self.assertFalse(func.is_pangram("I love Python"), '"I love Python" is not pangram')

    def test_pangram_with_other_characters(self):
        self.assertTrue(func.is_pangram("The*five@boxing!wizards^jump--quickly0"),
                        '"The*five@boxing!wizards^jump--quickly0" is pangram')