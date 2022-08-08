# Define date models
from dataclasses import dataclass


@dataclass
class FaresInputData:
    date_in: str
    date_out: str
    origin_airport_code: str
    destination_airport_code: str
    # Average prices if tehere more than one connection per day
    flatten_method: str = 'AVG'
