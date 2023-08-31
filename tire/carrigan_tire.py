from tire import Tire 

class CarriganTire(Tire):

    def __init__(self, reading : float):
        self.reading = reading

    def needs_service(self) -> bool:
        return self.reading >= 0.9