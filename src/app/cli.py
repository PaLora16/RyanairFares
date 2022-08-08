# parse command line parameter and fills FaresInputData object
# which carries requested parameters

from app.models import FaresInputData

from optparse import OptionParser


def fares_input_data() -> FaresInputData:
    parser = OptionParser()

    parser.add_option("-n", "--datein", dest="date_in",
                      help="start date to check fares")

    parser.add_option("-t", "--dateout", dest="date_out",
                      help="end date to check fares")

    parser.add_option("-o", "--iataori", dest="origin_airport_code",
                      help="IATA code of airport origin")

    parser.add_option("-d", "--iatades", dest="destination_airport_code",
                      help="IATA code of destibation origin")

    parser.add_option("-f", "--fares", dest="flatten_method",
                      help="values AVG,MAX,MIN show fares if more flights in one day AVG,MAX,MIN")

    (options, args) = parser.parse_args()

    return FaresInputData(options.date_in,
                          options.date_out,
                          options.origin_airport_code,
                          options.destination_airport_code,
                          options.flatten_method)

