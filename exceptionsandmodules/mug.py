
class Mug:

    def __init__(self, size_in_milliliters, color):
        self._size_in_milliliters = size_in_milliliters
        self._color = color
        self._current_volume_of_liquid_in_milliliters = 0

    def set_color(self, color):
        self._color = color

    def get_size_in_milliliters(self):
        return self._size_in_milliliters

    def get_color(self):
        return self._color

    def get_current_volume_of_liquid_in_milliliters(self):
        return self._current_volume_of_liquid_in_milliliters

    def fill(self):
        self._current_volume_of_liquid_in_milliliters = self._size_in_milliliters

    def drink(self, milliliters_to_drink):
        self._current_volume_of_liquid_in_milliliters -= milliliters_to_drink
        if self._current_volume_of_liquid_in_milliliters < 0:
            self._current_volume_of_liquid_in_milliliters = 0
            raise ValueError("You can't drink that many milliliters")

    def __str__(self):
        return f"{self.get_color()} color mug with {self.get_current_volume_of_liquid_in_milliliters()} " \
               f"of milliliters remaining out of {self.get_size_in_milliliters()}"

    def print_mug(self):
        print(f"{self.get_color()} color mug with {self.get_current_volume_of_liquid_in_milliliters()} "
              "of milliliters remaining out of {self.get_size_in_milliliters()}")
