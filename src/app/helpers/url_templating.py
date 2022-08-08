# Templates URL from config.py:
from app.config import Config

from app.models import FaresInputData


def get_fares_url(input_data: FaresInputData):
    return Config.FARES_URL.format(date_in=input_data.date_in,
                                   date_out=input_data.date_out,
                                   destination_airport_code=input_data.destination_airport_code,
                                   origin_airport_code=input_data.origin_airport_code)


def get_outbound_flights(origin_airport_code):
    return Config.AIRPORT_OUTBOUND_FLIGHTS_URL.format(origin_airport_code=origin_airport_code)


def get_flights_url(origin_airport_code,
                    destination_airport_code):
    return Config.FLIGHTS_URL.format(origin_airport_code=origin_airport_code,
                                     destination_airport_code=destination_airport_code)
