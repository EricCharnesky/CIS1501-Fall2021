import random


class PowerBallTicket:

    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self.value = random.randint(1, 10)

    def get_winnings(self, winning_ticket):
        if self.value == winning_ticket.value:
            return 10
        return 0