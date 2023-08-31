from tire import Tire 

class OctoprimeTire(Tire):

    total_reading = 0

    def __init__(self, reading : float):
        OctoprimeTire.total_reading += reading
        self.reading = reading

    def needs_service(self) -> bool:
        return OctoprimeTire.total_reading >= 3
