from typing import Dict, List


# based od CLI parameter reduce fares list to
# AVG - average price per day
# MIN - minimum price per day
# MAX - maximum price per day
# if there is more than 1 fligh per day
def fares_flatten(flatten_action: str, fares: Dict[str, List[str]]) -> Dict[str, str]:
    '''
    flatten_action - string with action to be performed on fares list
    return list of prices per day
    '''
    flattened_fares = {}
    for date, fare_day in fares.items():
        if flatten_action == 'AVG':
            flattened_fares[date] = str(
                round(sum(map(float, fare_day)) / len(fare_day), 2))
        elif flatten_action == 'MIN':
            flattened_fares[date] = str(min(map(float, fare_day)))
        elif flatten_action == 'MAX':
            flattened_fares[date] = str(max(map(float, fare_day)))
    return flattened_fares
