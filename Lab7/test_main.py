from unittest import TestCase
from main import Assignment

class TestAssignment(TestCase):


    def test_init(self):
        # arrange
        expected_name = 'Lab7'

        # act
        assignment = Assignment(expected_name)
        actual_name = assignment.get_name()

        # assert
        self.assertEqual(expected_name, actual_name)
