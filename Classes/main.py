class ElectricVehicle:

    def __init__(self, make, model, color, battery_capacity_in_kilowatt_hours, kilometers_per_kilowatt_hour):
        self._make = make
        self._model = model
        self.set_color(color)
        self._battery_capacity_in_kilowatt_hours = battery_capacity_in_kilowatt_hours
        self._kilometers_per_kilowatt_hour = kilometers_per_kilowatt_hour
        self._current_battery_charge_in_kilowatt_hours = 0

    def charge(self, kilowatt_hours_to_charge):
        if kilowatt_hours_to_charge > 0:
            self._current_battery_charge_in_kilowatt_hours += kilowatt_hours_to_charge

            if self._current_battery_charge_in_kilowatt_hours > self._battery_capacity_in_kilowatt_hours:
                self._current_battery_charge_in_kilowatt_hours = self._battery_capacity_in_kilowatt_hours

    def drive(self, kilometers_to_drive):
        if kilometers_to_drive > 0:
            kilowatt_hours_required = kilometers_to_drive / self._kilometers_per_kilowatt_hour
            self._current_battery_charge_in_kilowatt_hours -= kilowatt_hours_required

            if self._current_battery_charge_in_kilowatt_hours < 0:
                self._current_battery_charge_in_kilowatt_hours = 0
                return False

            return True

        return False

    def set_color(self, color):
        self._color = color

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def get_battery_capacity_in_kilowatt_hours(self):
        return self._battery_capacity_in_kilowatt_hours

    def get_kilometers_per_kilowatt_hour(self):
        return self._kilometers_per_kilowatt_hour

    def get_current_battery_charge_in_kilowatt_hours(self):
        return self._current_battery_charge_in_kilowatt_hours


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

    def __str__(self):
        return f"{self.get_color()} color mug with {self.get_current_volume_of_liquid_in_milliliters()} " \
               f"of milliliters remaining out of {self.get_size_in_milliliters()}"

    def print_mug(self):
        print(f"{self.get_color()} color mug with {self.get_current_volume_of_liquid_in_milliliters()} "
              "of milliliters remaining out of {self.get_size_in_milliliters()}")


def print_mug(mug):
    print(f"{mug.get_color()} color mug with {mug.get_current_volume_of_liquid_in_milliliters()} "
          f"of milliliters remaining out of {mug.get_size_in_milliliters()}")


#               calls the __init__ method
marathon_mug = Mug(250, "white with blue edges")

chessbrah_mug = Mug(300, "grey")

marathon_mug.print_mug()
print_mug(chessbrah_mug)

# awkward way to call the method
Mug.fill(marathon_mug)
marathon_mug.fill()
chessbrah_mug.fill()

marathon_mug.drink(50)
chessbrah_mug.drink(10000)

print_mug(marathon_mug)
print_mug(chessbrah_mug)

print(marathon_mug)
print(chessbrah_mug)


bolt = ElectricVehicle("chevy", "bolt", "grey", 80, 3.3)

