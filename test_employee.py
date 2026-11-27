import unittest

from employee_bonus import calculate_annual_bonus


class TestEmployeeBonus(unittest.TestCase):

    # ------------------------
    # Normal Test Cases
    # ------------------------

    def test_rating_5_bonus(self):
        self.assertEqual(
            calculate_annual_bonus(100000, 5),
            20000
        )

    def test_rating_4_bonus(self):
        self.assertEqual(
            calculate_annual_bonus(80000, 4),
            12000
        )

    def test_rating_3_bonus(self):
        self.assertEqual(
            calculate_annual_bonus(60000, 3),
            6000
        )

    # ------------------------
    # Boundary Test Cases
    # ------------------------

    def test_minimum_rating(self):
        self.assertEqual(
            calculate_annual_bonus(50000, 1),
            0
        )

    def test_maximum_rating(self):
        self.assertEqual(
            calculate_annual_bonus(50000, 5),
            10000
        )

    def test_zero_salary(self):
        self.assertEqual(
            calculate_annual_bonus(0, 4),
            0
        )

    # ------------------------
    # Invalid Input Tests
    # ------------------------

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            calculate_annual_bonus(-1000, 4)

    def test_rating_below_range(self):
        with self.assertRaises(ValueError):
            calculate_annual_bonus(50000, 0)

    def test_rating_above_range(self):
        with self.assertRaises(ValueError):
            calculate_annual_bonus(50000, 6)

    def test_salary_as_string(self):
        with self.assertRaises(TypeError):
            calculate_annual_bonus("50000", 4)

    def test_rating_as_string(self):
        with self.assertRaises(TypeError):
            calculate_annual_bonus(50000, "4")


if __name__ == "__main__":
    unittest.main()