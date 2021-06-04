from typing import Any, Dict, List

from requests.exceptions import HTTPError

from carpathian_beer.entity.beer import Beer
from carpathian_beer.exceptions.carpathian_beer_exceptions import InvalidIdException
from carpathian_beer.session.request_session import RequestSession


class PunkApiClient:
    def __init__(
        self,
        base_url: str = "https://api.punkapi.com/v2/beers",
        session: RequestSession = RequestSession(),
    ) -> None:
        self.__base_url = base_url
        self.__session = session

    Params = Dict[str, str]

    def __get_response(self, params: Params = None, url_option: str = None) -> Any:
        if params:
            response = self.__session.get(self.__base_url, params)
        if url_option:
            response = self.__session.get(f"{self.__base_url}/{url_option}")
        response.raise_for_status()
        return response.json()

    def get_beer(self, id: int) -> Beer:
        try:
            response = self.__get_response(url_option=id)
            return Beer(response[0])
        except HTTPError as error:
            raise InvalidIdException(error)

    def get_random_beer(self) -> Beer:
        response = self.__get_response(url_option="random")
        return Beer(response[0])

    Beers = List[Beer]

    def get_all_beers(
        self, page: int = None, per_page: int = 25, limit: int = None
    ) -> Beers:
        # Get beers from the API
        # Output: beers - list
        if not page:
            page = 1
            per_page = 80

        if not limit:
            limit = per_page

        response = self.__get_response(params={"page": page, "per_page": per_page})
        while len(response) < limit:
            page += 1
            response += self.__get_response(params={"page": page, "per_page": per_page})

        beers = []
        for beer_details in response[:limit]:
            beers.append(Beer(beer_details))
        return beers

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_iter_all_beers(self) -> Beer:
        beers = self.get_all_beers()
        for beer in beers:
            yield beer

    def get_beers_brewd_before(self, month: int = None, year: int = None) -> Beers:
        # Get beers brewed before (month-year)
        response = self.__get_response(params={"brewed_before": f"{month}-{year}"})
        beers = []
        for beer_details in response:
            beers.append(Beer(beer_details))
        return beers
