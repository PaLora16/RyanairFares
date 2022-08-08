
import sys
from app.cli import fares_input_data
from app.api.fares import get_fares
from app.api.airports import get_all_airports
from app.input_verify.airport_verify import is_airport_code_valid
from app.input_verify.date_verify import is_date_format_valid
from app.input_verify.date_verify import are_dates_valid
from app.input_verify.airport_verify import has_aiport_ryanair_connection
from app.input_verify.airport_verify import has_airport_outbound_connection
from app.models import FaresInputData
from app.helpers.fares import fares_flatten
from app.presentation.matplotlib_view import plot_fares

from typing import List, Tuple

# cached airports
all_airports: List[Tuple[str, str]] = get_all_airports()


# Print error message and exit app
def resolve_error(error_message: str) -> None:
    print(error_message)
    sys.exit(1)


def verify_route(input_data: FaresInputData) -> None:
    if not has_airport_outbound_connection(input_data.origin_airport_code,
                                           input_data.destination_airport_code):
        resolve_error(
            f'There is no connection from {input_data.origin_airport_code} to {input_data.destination_airport_code} between {input_data.date_in} and {input_data.date_out}')


def verify_airport_origin(input_data: FaresInputData) -> None:
    if not has_aiport_ryanair_connection(input_data.origin_airport_code):
        resolve_error(
            f'Origin airport {input_data.origin_airport_code} has no Ryanair connection')


# Check origin and destination airport code validity
def verify_airport_code(input_data: FaresInputData) -> None:
    if not is_airport_code_valid(input_data.origin_airport_code, all_airports):
        resolve_error(
            f'Origin airport code {input_data.origin_airport_code} is not valid')
    if not is_airport_code_valid(input_data.destination_airport_code, all_airports):
        resolve_error(
            f'Destination airport code {input_data.destination_airport_code} is not valid')


def verify_date_format(input_data: FaresInputData) -> None:
    if not is_date_format_valid(input_data.date_in):
        resolve_error(
            f'Date in {input_data.date_in} is not valid. Check format yyyy-mm-dd or days in months')
    if not is_date_format_valid(input_data.date_out):
        resolve_error(
            f'Date out {input_data.date_out} is not valid. Check format yyyy-mm-dd or days in months')


# Verify if Date out is >= Date in
def verify_date(input_data: FaresInputData) -> None:
    if not are_dates_valid(input_data.date_in, input_data.date_out):
        resolve_error(
            f'{input_data.date_out} must be greater or equal to {input_data.date_in} ')


def run_app():
    try:
        # raw data from command line
        input_data: FaresInputData = fares_input_data()
        verify_airport_code(input_data)
        verify_date_format(input_data)
        verify_date(input_data)
        verify_airport_origin(input_data)
        verify_route(input_data)
        fares = get_fares(input_data)
        fares = fares_flatten(input_data.flatten_method, fares)
        plot_fares(fares, input_data)
    except Exception as e:
        resolve_error(str(e))
