from punk_api_exception import PunkAPIException

from entity.beer import Beer
from session.request_session import RequestSession


class PunkApiClient:
    def __init__(
        self, base_url="https://api.punkapi.com/v2/beers", session=RequestSession()
    ):
        self.__base_url = base_url
        self.__session = session

    def get_response(self, url_option):
        # Get response for request
        # Input: url_option - string
        # Output: response - object
        # Raise PunkAPIException if url is invalid
        try:
            response = self.__session.get(f"{self.__base_url}{url_option}")
            response.raise_for_status()
            return response.json()
        except Exception:
            # Carpathian_beer Exception !
            raise PunkAPIException("")

    # Impartim in 2 !
    def get_beer(self, id=None):
        # Get a single beer form the API using the beer's id
        # If id == random: returns a random beer
        # Output: Beer - object
        try:
            if id:
                response = self.get_response(f"/{id}")
            else:
                response = self.get_response("/random")
            return Beer(response[0])
        except PunkAPIException as exception:
            # Clasa de exceptie care prinda usecase => RAISE "id invalid"
            return exception

    # Nr de beers
    # Generator peste care pot sa iterez : get_iter_all_bears
    # Lista cu toate berile in alta functie !
    # Fara PunkAPIException ..
    def get_all_beers(self):
        # Get beers from the API
        # Output: beers - list
        response = self.get_response("")
        beers = []
        for beer_details in response:
            beers.append(Beer(beer_details))
        return beers

    def get_beers_brewd_before(self, month=None, year=None):
        # Get beers brewed before (month-year)

        try:
            if month and year:
                response = self.get_response(f"?brewed_before={month}-{year}")
                beers = []
                for beer_details in response:
                    beers.append(Beer(beer_details))
                return beers
            else:
                return []
        except PunkAPIException as exception:
            return exception
