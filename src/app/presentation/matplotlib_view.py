import matplotlib.pyplot as plt
from typing import Dict

from app.models import FaresInputData


# plot prices per day x days of selected Ryanair connections
def plot_fares(fares: Dict[str, str], input_data: FaresInputData) -> None:
    sorted_fares = dict(sorted(fares.items(), key=lambda x: x[0]))

    x = []
    y = []

    for date, price in sorted_fares.items():
        x.append(date)
        y.append(float(price))

    # Title
    fares_type = "average" if input_data.flatten_method == "AVG" else "minimum" if input_data.flatten_method == "MIN" else "maximum"

    plt.title(
        f'Ryanair {fares_type} fares from {input_data.origin_airport_code} to {input_data.destination_airport_code}')

    # naming the x-axis
    plt.xlabel('Day ->')

    # naming the y-axis
    plt.ylabel('Price ->')

    plt.plot(x, y)
    plt.show()
