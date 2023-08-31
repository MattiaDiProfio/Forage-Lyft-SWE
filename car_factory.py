from datetime import date
from car import Car
from typing import List
# engine related classes
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
# battery related classes
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
#tire related classes
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory:

    def create_calliope(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_wear : List[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = [CarriganTire(tire_wear[0]), CarriganTire(tire_wear[1]), CarriganTire(tire_wear[2]), CarriganTire(tire_wear[3])]
        return Car(engine, battery, tires)

    def create_glissade(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_wear : List[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = [OctoprimeTire(tire_wear[0]), OctoprimeTire(tire_wear[1]), OctoprimeTire(tire_wear[2]), OctoprimeTire(tire_wear[3])]
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date : date, last_service_date : date, warning_light_is_on : bool, tire_wear : List[float]) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = [CarriganTire(tire_wear[0]), CarriganTire(tire_wear[1]), CarriganTire(tire_wear[2]), CarriganTire(tire_wear[3])]
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_wear : List[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = [OctOctoprimeTire(tire_wear[0]), OctoprimeTire(tire_wear[1]), OctoprimeTire(tire_wear[2]), OctoprimeTire(tire_wear[3])]
        return Car(engine, battery, tires)

    def create_thovex(self, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_wear : List[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = [CarriganTire(tire_wear[0]), CarriganTire(tire_wear[1]), CarriganTire(tire_wear[2]), CarriganTire(tire_wear[3])]
        return Car(engine, battery, tires)
