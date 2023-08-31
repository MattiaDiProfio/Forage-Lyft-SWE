from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire
from typing import List

class Car(Serviceable):

    def __init__(self, engine : Engine, battery : Battery, tires : List[Tire]):
        self.engine = engine    
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        #check if tires need to be serviced
        for tire in self.tires:
            if (tire.needs_service()):
                return True
        return (self.engine.needs_service() or self.battery.needs_service())