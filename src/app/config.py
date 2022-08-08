class Config(object):

    ALL_AIRPORTS_URL = "https://www.ryanair.com/api/locate/v1/autocomplete/airports?phrase&market=en-gb"
    AIRPORT_OUTBOUND_FLIGHTS_URL = "https://www.ryanair.com/api/locate/v1/autocomplete/routes?arrivalPhrase&departurePhrase={origin_airport_code}&market=en-gb"
    FLIGHTS_URL = "https://www.ryanair.com/api/farfnd/3/oneWayFares/{origin_airport_code}/{destination_airport_code}/availabilities"
    FARES_URL = "https://www.ryanair.com/api/booking/v4/en-gb/availability?ADT=1&CHD=0&DateIn={date_in}&DateOut={date_out}&Destination={destination_airport_code}&Disc=0&INF=0&Origin={origin_airport_code}&TEEN=0&promoCode&IncludeConnectingFlights=false&FlexDaysBeforeOut=2&FlexDaysOut=2&ToUs=AGREED"
