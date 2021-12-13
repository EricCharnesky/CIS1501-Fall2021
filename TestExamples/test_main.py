from unittest import TestCase
from main import PowerBallTicket


class TestPowerBallTicket(TestCase):

    def test_get_winnings_wins10(self):
        # arrange
        expected_winnings = 10
        my_ticket = PowerBallTicket(42)
        winning_ticket = PowerBallTicket(42)

        # act
        actual_winnings = my_ticket.get_winnings(winning_ticket)

        # assert
        self.assertEquals(expected_winnings, actual_winnings)

    def test_get_winnings_loss(self):
        # arrange
        expected_winnings = 0
        my_ticket = PowerBallTicket(42)
        winning_ticket = PowerBallTicket(43)

        # act
        actual_winnings = my_ticket.get_winnings(winning_ticket)

        # assert
        self.assertEquals(expected_winnings, actual_winnings)
