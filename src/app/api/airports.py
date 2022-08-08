from typing import Tuple, List
import requests

from app.config import Config


def get_all_airports() -> List[Tuple[str, str]]:
    """
    Get all airports from Ryanair API
    """
    all_airports = requests.get(Config.ALL_AIRPORTS_URL).json()
    return _get_airport_codes(all_airports)


def _get_airport_codes(all_airports) -> List[Tuple[str, str]]:
    """flatten airports to list of tuples"""
    return [(airport['code'], airport['name']) for airport in all_airports]
