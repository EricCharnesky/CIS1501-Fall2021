from unittest import TestCase
# from name_of_py_file import name_of_class
from main import ElectricVehicle


class TestElectricVehicle(TestCase):

    def test_init(self):
        # AAA Convention

        # arrange all of our variables that we need for testing
        expected_make = "Chevy"
        expected_model = "Bolt"
        expected_color = "Grey"
        expected_capacity_in_kilowatt_hours = 80
        expected_kilometers_per_kilowatt_hour = 3.3
        expected_current_charge_in_kilowatt_hours = 0

        # act - actually call the code we are testing, and get values
        electric_vehicle = ElectricVehicle(
            expected_make, expected_model, expected_color,
            expected_capacity_in_kilowatt_hours,
            expected_kilometers_per_kilowatt_hour)
        actual_make = electric_vehicle.get_make()
        actual_model = electric_vehicle.get_model()
        actual_color = electric_vehicle.get_color()
        actual_battery_capacity_in_kilowatt_hours = electric_vehicle.get_battery_capacity_in_kilowatt_hours()
        actual_kilometers_per_kilowatt_hour = electric_vehicle.get_kilometers_per_kilowatt_hour()
        actual_current_charge_in_kilowatt_hours = electric_vehicle.get_current_battery_charge_in_kilowatt_hours()

        # assert - did we get what we expected
        self.assertEqual(expected_make, actual_make)
        self.assertEqual(expected_model, actual_model)
        self.assertEqual(expected_color, actual_color)
        self.assertEqual(expected_capacity_in_kilowatt_hours, actual_battery_capacity_in_kilowatt_hours)
        self.assertEqual(expected_kilometers_per_kilowatt_hour, actual_kilometers_per_kilowatt_hour)
        self.assertEqual(expected_current_charge_in_kilowatt_hours, actual_current_charge_in_kilowatt_hours)

    def test_charge(self):
        # arrange
        capacity_in_kilowatt_hours = 80
        electric_vehicle = ElectricVehicle("", "", "", capacity_in_kilowatt_hours, 0)

        # act
        electric_vehicle.charge(capacity_in_kilowatt_hours + 1)
        actual_current_charge_in_kilowatt_hours = electric_vehicle.get_current_battery_charge_in_kilowatt_hours()

        # assert
        self.assertEqual(capacity_in_kilowatt_hours, actual_current_charge_in_kilowatt_hours)

    def test_drive_returns_true(self):
        # arrange
        electric_vehicle = ElectricVehicle("", "", "", 80, 10)
        electric_vehicle.charge(80)
        expected_current_charge_in_kilowatt_hours = 79

        # act
        result = electric_vehicle.drive(10)
        actual_current_charge_in_kilowatt_hours = electric_vehicle.get_current_battery_charge_in_kilowatt_hours()

        # assert
        self.assertTrue(result)
        self.assertEqual(expected_current_charge_in_kilowatt_hours, actual_current_charge_in_kilowatt_hours)

    def test_drive_returns_false_when_using_all_battery(self):
        # arrange
        electric_vehicle = ElectricVehicle("", "", "", 80, 10)
        electric_vehicle.charge(1)
        expected_current_charge_in_kilowatt_hours = 0

        # act
        result = electric_vehicle.drive(11)
        actual_current_charge_in_kilowatt_hours = electric_vehicle.get_current_battery_charge_in_kilowatt_hours()

        # assert
        self.assertFalse(result)
        self.assertEqual(expected_current_charge_in_kilowatt_hours, actual_current_charge_in_kilowatt_hours)

    def test_drive_negative_value_returns_false(self):
        # arrange
        electric_vehicle = ElectricVehicle("", "", "", 80, 10)
        expected_current_charge_in_kilowatt_hours = 0

        # act
        result = electric_vehicle.drive(-1)
        actual_current_charge_in_kilowatt_hours = electric_vehicle.get_current_battery_charge_in_kilowatt_hours()

        # assert
        self.assertFalse(result)
        self.assertEqual(expected_current_charge_in_kilowatt_hours, actual_current_charge_in_kilowatt_hours)
