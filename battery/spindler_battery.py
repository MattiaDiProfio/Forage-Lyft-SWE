from battery import Battery 
from datetime import date, datetime

class SpindlerBattery(Battery):

    def __init__(self, last_service_date : date, current_date : date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        last_service_year = self.last_service_date.year
        current_year = self.current_date.year
        return abs(current_year - last_service_year) > 2
