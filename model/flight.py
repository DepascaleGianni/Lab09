from dataclasses import dataclass
from datetime import date
@dataclass
class Flight:
    _id: int
    _airline_id: int
    _flight_number:int
    _tail_number : str
    _origin_airport_id : int
    _destination_airport_id : int
    #_scheduled_departure_date : date
    #_departure_delay : int
    #_elapsed_time : int
    _distance : int
    #_arrival_date : date
    #_arrival_delay : int

    @property
    def distance (self):
        return self._distance

    @property
    def id (self):
        return self._id

    @property
    def airline_id(self):
        return self._airline_id

    @property
    def origin_airport_id(self):
        return self._origin_airport_id
    @property
    def destination_airport_id(self):
        return self._destination_airport_id

