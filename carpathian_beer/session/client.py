import logging
from typing import Any, Dict, List, Union

from requests.exceptions import HTTPError

from carpathian_beer import Beer, InvalidIdException, RequestSession

Beers = List[Beer]
Params = Dict[str, str]
IntOrString = Union[int, str]


class Client:
    def __init__(
        self,
        base_url: str = "https://api.punkapi.com/v2/beers",
        session: RequestSession = RequestSession(),
    ) -> None:
        self.__base_url = base_url
        self.__session = session
        logging.info("PunkApiClient object has been initialized")

    def __get_response(self, url: str = None, params: Params = None) -> Dict[str, Any]:
        if not url:
            url = self.__base_url
        response = self.__session.get(url, params)
        response.raise_for_status()
        logging.info("__get_response has been called")
        return response.json()

    def get_beer(self, id: int) -> Beer:
        logging.info("get_beer has been called")
        try:
            url = f"{self.__base_url}/{id}"
            response = self.__get_response(url)
            return Beer(**response[0])
        except HTTPError as error:
            logging.error("HTTPError occured")
            raise InvalidIdException(error)

    def get_random_beer(self) -> Beer:
        url = f"{self.__base_url}/random"
        response = self.__get_response(url)
        logging.info("get_random_beer has been called")
        return Beer(**response[0])

    def get_all_beers(
        self,
        page: IntOrString = None,
        per_page: IntOrString = 25,
        limit: IntOrString = None,
    ) -> Beers:
        logging.info("get_all_beers has been called")
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
            beers.append(Beer(**beer_details))
        return beers

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_iter_all_beers(self) -> Beer:
        logging.info("get_iter_all_beers has been called")
        beers = self.get_all_beers()
        for beer in beers:
            yield beer

    def get_beers_brewd_before(self, month: int = None, year: int = None) -> Beers:
        # Get beers brewed before (month-year)
        logging.info("get_beers_brewd_before has been called")
        response = self.__get_response(params={"brewed_before": f"{month}-{year}"})
        beers = []
        for beer_details in response:
            beers.append(Beer(**beer_details))
        return beers
