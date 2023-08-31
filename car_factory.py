from datetime import date
from car import Car
# engine related classes
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
# battery related classes
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory:

    def create_calliope(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date : date, last_service_date : date, warning_light_is_on : bool) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
