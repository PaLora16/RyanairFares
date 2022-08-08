# Verify start and end date input
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def is_date_format_valid(checked_date: str) -> bool:
    """
    Verify if expected date format yyyy-mm-dd 
    """
    _is_valid = True
    try:
        datetime.strptime(checked_date, DATE_FORMAT)
    except ValueError:
        _is_valid = False
    return _is_valid


# Verifies if end date is >= start_date
def are_dates_valid(date_in: str, date_out: str) -> bool:
    date_in_obj = datetime.strptime(date_in, DATE_FORMAT)
    date_out_obj = datetime.strptime(date_out, DATE_FORMAT)
    return date_out_obj >= date_in_obj
