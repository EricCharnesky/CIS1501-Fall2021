from unittest import TestCase
from main import Assignment

class TestAssignment(TestCase):


    def test_init(self):
        # arrange
        expected_name = 'Lab7'
        expected_points_possible = 10
        expected_earned = 10

        # act
        assignment = Assignment(expected_name, expected_points_possible, expected_earned)
        actual_name = assignment.get_name()
        actual_points_possible = assignment.get_points_possible()
        actual_points_earned = assignment.get_points_earned()

        # assert
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_points_possible, actual_points_possible)
        self.assertEqual(expected_earned, actual_points_earned)

    def test_set_points_earned_negative(self):
        # arrange
        points_possible = 10
        expected_earned = 0

        # act
        assignment = Assignment("", points_possible, -1)
        actual_points_earned = assignment.get_points_earned()

        # assert
        self.assertEqual(expected_earned, actual_points_earned)

    def test_set_points_earned_more_than_possible(self):
        # arrange
        points_possible = 10
        expected_earned = 10

        # act
        assignment = Assignment("", points_possible, 20)
        actual_points_earned = assignment.get_points_earned()

        # assert
        self.assertEqual(expected_earned, actual_points_earned)

    def test_get_letter_grade_a(self):
        # arrange
        points_possible = 10
        points_earned = 10
        expected_letter_grade = 'A'

        # act
        assignment = Assignment("", points_possible, points_earned)
        actual_letter_grade = assignment.get_letter_grade()

        # assert
        self.assertEqual(expected_letter_grade, actual_letter_grade)

    def test_get_letter_grade_cplus(self):
        # arrange
        points_possible = 100
        points_earned = 78
        expected_letter_grade = 'C+'

        # act
        assignment = Assignment("", points_possible, points_earned)
        actual_letter_grade = assignment.get_letter_grade()

        # assert
        self.assertEqual(expected_letter_grade, actual_letter_grade)