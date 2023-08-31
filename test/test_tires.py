import unittest
from datetime import datetime

import sys 
sys.path.append('C:\\Users\\matti\\OneDrive\\Desktop\\Forage-Lyft-Code')

from car_factory import CarFactory

class TestCarriganTires(unittest.TestCase):

    car_factory = CarFactory()

    def test_carrigan_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0

        car = self.car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, [0.5, 0.1, 0.96, 0.4])
        self.assertTrue(car.needs_service())

    def test_carrigan_tires_not_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0

        car = self.car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, [0.5, 0.1, 0.8, 0.4])
        self.assertFalse(car.needs_service())


class TestOctoprimeTires(unittest.TestCase):

    car_factory = CarFactory()

    def test_octoprime_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0

        car = self.car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, [0.8, 0.8, 0.8, 0.8])
        self.assertTrue(car.needs_service())

    def test_octoprime_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0

        car = self.car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, [0.5, 0.5, 0.5, 0.5])
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
