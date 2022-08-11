### Ryanair fares comparision

This demo features actual data from Ryanair public backends, enabling visualizing a set of
fares between departure and arrival airports in a given date period. Airports are given by IATA codes. Dates have format yyyy-mm-dd.
This version depends on the CLI interface as the main purpose is to show good developer practice.
This demo features JMESPath - a cool library allowing easy traverse of JSON or dict objects. Filtering, searching etc. of complex JSON schema is a piece of cake. For more info, see [jmespath](https://jmespath.org/tutorial.html)

### Options

Apps is CLI base with following parameters:

    -n dateIn start date to check fares
    -t dateOut end day to check fares 
    -o origin airport IATA code
    -d destination airport IATA code
    -f <AVG|MAX|MIN> If there are more flights on route per day, fares shown AVG - average, MAX - maximum, MIN - minimum fares of all flights.
        if not specified, AVG option is implicitly specified.

### Run example

- clone app to any local folder
- cd to src folder
- activate virtual env
- install from PyPi libraries - see Requirements
- run example : python ryanair.py -n  2022-09-10 -t 2022-09-30 -o STN -d ORK -f MAX

### Python version

Tested on 3.9

### Requirements

jmespath,
matplotlib
requests

### Improvements

- check and add missing typing
- improve response time employing async backend requests
- improve logging
- add unit tests
- Verify on CLI level enums of -f parameter
