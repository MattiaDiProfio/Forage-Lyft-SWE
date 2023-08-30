from battery import Battery 
from datetime import date, datetime

class NubbinBattery(Battery):

    def __init__(self, last_service_date : date, current_date : date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (datetime.strptime(self.current_date, "%m-%d-%Y") - datetime.strptime(self.last_service_date, "%m-%d-%Y")).days > (2 * 365)