from typing import List, Tuple
import requests

from app.helpers.url_templating import get_outbound_flights
from app.helpers.url_templating import get_flights_url


# Check if airport code is valid = in list of aiports from backend
def is_airport_code_valid(airport_code: str, all_airports: List[Tuple[str, str]]) -> bool:
    airport_code = airport_code.upper().strip()
    return any(airport[0] == airport_code for airport in all_airports)


# Calls Ryanair backend to check if airport has Ryanair connection anywhere
def has_aiport_ryanair_connection(origin_airport_code: str) -> bool:
    '''
    origin_airport_code - verified airport code
    return True if no empty connection list else False
    '''
    url = get_outbound_flights(origin_airport_code)
    return requests.get(url).json()


# For particular airport checks if Ryanair has flights to destination airport
def has_airport_outbound_connection(origin_airport_code: str,
                                    destination_airport_code: str) -> bool:
    """
    check if Ryanair has flights from origin airport to destination airport   
    """
    url = get_flights_url(origin_airport_code, destination_airport_code)
    connections = requests.get(url).json()
    return bool(connections)
