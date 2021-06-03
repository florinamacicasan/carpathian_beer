from requests.exceptions import HTTPError

from carpathian_beer.entity.beer import Beer
from carpathian_beer.exceptions.carpathian_beer_exceptions import InvalidIdException
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

        # params pentru get !!
        # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
        response = self.__session.get(f"{self.__base_url}{url_option}")
        response.raise_for_status()
        return response.json()

    def get_beer(self, id):
        try:
            response = self.__get_response(f"/{id}")
            return Beer(response[0])
        except HTTPError:
            raise InvalidIdException()

    def get_random_beer(self):
        response = self.__get_response("/random")
        return Beer(response[0])

    # raname from_page -> page
    def get_all_beers(self, from_page=None, per_page=25, limit=None):
        # Get beers from the API
        # Output: beers - list
        if not from_page:
            from_page = 1
            per_page = 80

        if not limit:
            limit = per_page

        # query params
        response = self.__get_response(f"?page={from_page}&per_page={per_page}")
        while len(response) < limit:
            from_page += 1
            response += self.__get_response(f"?page={from_page}&per_page={per_page}")

        beers = []
        for beer_details in response[:limit]:
            beers.append(Beer(beer_details))
        return beers

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_iter_all_beers(self):
        beers = self.get_all_beers()
        for beer in beers:
            yield beer

    def get_beers_brewd_before(self, month=None, year=None):
        # Get beers brewed before (month-year)
        response = self.__get_response(f"?brewed_before={month}-{year}")
        beers = []
        for beer_details in response:
            beers.append(Beer(beer_details))
        return beers
