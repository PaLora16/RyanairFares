import requests
import jmespath
from typing import Dict, List

from app.helpers.url_templating import get_fares_url
from app.models import FaresInputData


# read from Ryanair backend fares for  given period and airports
def get_fares(input_data: FaresInputData) -> Dict[str, List[str]]:
    url = get_fares_url(input_data)
    fares = requests.get(url).json()
    i = 0
    # List of prices per day
    dates_out = {}
    while True:
        raw_date = jmespath.search(f'trips[0].dates[{i}].dateOut', fares)
        if not raw_date:
            break
        # just date portion from datetime string
        # dateOut is a key for references to prices all flights given day
        date_out = raw_date[:10]
        # list
        amounts = []
        j = 0
        # each day there can be nmore flights in given destination. If so,
        # amounts contains list of prices per flight
        while True:
            amount = jmespath.search(
                f'trips[0].dates[{i}].flights[{j}].regularFare.fares[0].amount', fares)
            if not amount:
                break
            amounts.append(amount)
            j += 1
        # key - date of connection, value - list of prices per flight if more flights this day
        dates_out[date_out] = amounts
        # next day
        i += 1
    return dates_out
