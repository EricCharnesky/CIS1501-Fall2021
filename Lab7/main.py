class Assignment:

    def __init__(self, name, points_possible, points_earned):
        self._name = name
        self._points_possible = points_possible
        self.set_points_earned(points_earned)

    def get_name(self):
        return self._name

    def get_points_possible(self):
        return self._points_possible

    def get_points_earned(self):
        return self._points_earned

    def get_letter_grade(self):
        percentage = self._points_earned / self._points_possible
        if percentage >= .93:
            return "A"
        elif percentage >= .90:
            return "A-"
        elif percentage >= .87:
            return "B+"
        elif percentage >= .83:
            return "B"
        elif percentage >= .80:
            return "B-"
        elif percentage >= .77:
            return "C+"
        elif percentage >= .73:
            return "C"
        elif percentage >= .70:
            return "C-"
        elif percentage >= .67:
            return "D+"
        elif percentage >= .63:
            return "D"
        else:
            return "F"

    def set_points_earned(self, points_earned):
        if points_earned < 0:
            self._points_earned = 0
        elif points_earned > self._points_possible:
            self._points_earned = self._points_possible
        else:
            self._points_earned = points_earned