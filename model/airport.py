from dataclasses import dataclass

@dataclass
class Airport:
    _id : int
    _iata_code : str
    _airport : str
    #_city : str
    #_state : str
    #_country : str
    #_latitude : int
    #_longitude : int
    #_timezone_offset : int

    @property
    def id(self):
        return self._id

    @property
    def airport(self):
        return self._airport

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f'airport {self._airport} - id : {self._id}'