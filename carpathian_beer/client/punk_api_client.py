from carpathian_beer.entity.beer import Beer
from carpathian_beer.exceptions.punk_api_exception import PunkAPIException
from carpathian_beer.session.request_session import RequestSession


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

    def get_beer(self, id):
        try:
            response = self.get_response(f"/{id}")
            return Beer(response[0])
        except Exception:
            # Clasa de exceptie care prinda usecase => RAISE "id invalid"
            raise PunkAPIException('id invalid')

    def get_random_beer(self):
        try:
            response = self.get_response("/random")
            return Beer(response[0])
        except Exception:
            # Clasa de exceptie care prinda usecase => RAISE "id invalid"
            raise PunkAPIException('url invalid')

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_all_beers(self):
        # Get beers from the API
        # Output: beers - list
        response = self.get_response("?page=13&per_page=25")
        beers = []
        for beer_details in response:
            beers.append(Beer(beer_details))
        return beers

    def get_iter_all_beers(self):
        beers=self.get_all_beers()
        for beer in beers:
            yield beer


    def get_beers_brewd_before(self, month=None, year=None):
        # Get beers brewed before (month-year)
        if month and year:
            response = self.get_response(f"?brewed_before={month}-{year}")
            beers = []
            for beer_details in response:
                beers.append(Beer(beer_details))
            return beers
        else:
            return []

def main():
    client=PunkApiClient()
    print(client.get_iter_all_beers())

main()