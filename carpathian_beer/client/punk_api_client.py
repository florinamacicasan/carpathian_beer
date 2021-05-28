from requests.exceptions import HTTPError

from carpathian_beer.entity.beer import Beer
from carpathian_beer.exceptions.carpathian_beer_exceptions import (
    InvalidIdException,
    InvalidMonthOrYearException,
)
from carpathian_beer.session.request_session import RequestSession


class PunkApiClient:
    def __init__(
        self, base_url="https://api.punkapi.com/v2/beers", session=RequestSession()
    ):
        self.__base_url = base_url
        self.__session = session

    def __get_response(self, url_option):
        # Get response for request
        # Input: url_option - string
        # Output: response - object
        response = self.__session.get(f"{self.__base_url}{url_option}")
        response.raise_for_status()
        return response.json()

    def get_beer(self, id):
        try:
            response = self.__get_response(f"/{id}")
            return Beer(response[0])
        except HTTPError or Exception:
            raise InvalidIdException()

    def get_random_beer(self):
        response = self.__get_response("/random")
        return Beer(response[0])

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_all_beers(self):
        # Get beers from the API
        # Output: beers - list
        response = self.__get_response("?page=13&per_page=25")
        beers = []
        for beer_details in response:
            beers.append(Beer(beer_details))
        return beers

    def get_iter_all_beers(self):
        beers = self.get_all_beers()
        for beer in beers:
            yield beer

    def __validate_month_and_year(self, month, year):
        try:
            month = int(month)
            year = int(year)
            if 0 < month and month <= 12 and 0 < year:
                return True
            return False
        except ValueError:
            return False

    def get_beers_brewd_before(self, month=None, year=None):
        # Get beers brewed before (month-year)
        if month and year:
            if self.__validate_month_and_year(month, year):
                response = self.__get_response(f"?brewed_before={month}-{year}")
                beers = []
                for beer_details in response:
                    beers.append(Beer(beer_details))
                return beers
            else:
                raise InvalidMonthOrYearException()
        else:
            return []
