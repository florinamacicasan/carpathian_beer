import logging
from typing import Any, Dict, List, Union

from requests.exceptions import HTTPError
from carpathian_beer import Beer, RequestSession, InvalidIdException, ArgumentsException


Beers = List[Beer]
Params = Dict[str, str]
IntOrString = Union[int, str]


class Client:
    def __init__(
        self,
        base_url: str = "https://api.punkapi.com/v2/beers",
        session: RequestSession = RequestSession(),
        shouldLog: bool = False,
    ) -> None:
        self.__base_url = base_url
        self.__session = session
        self.__shouldLog = shouldLog

    def log_if_requested(function):
        def wrapper(self, *args, **kwargs):
            if self.__shouldLog:
                logging.info(
                    f"{function.__name__} called with arguments {args}, {kwargs}"
                )

            try:
                result = function(self, *args, **kwargs)
                info = {}
                if type(result) is list and len(result) > 0:
                    info["size"] = len(result)
                    info["first object"] = result[0]
                    info["last object"] = result[-1]
                else:
                    info["object"] = result

            except Exception as exception:
                logging.error(f"{exception} occured")
                raise exception

            if self.__shouldLog:
                logging.info(f"{function.__name__} returned {info}")
            return result

        return wrapper

    def __get_response(self, url: str = None, params: Params = None) -> Dict[str, Any]:
        if not url:
            url = self.__base_url
        response = self.__session.get(url, params)
        response.raise_for_status()
        return response.json()

    @log_if_requested
    def get_beer(self, id: int) -> Beer:
        try:
            url = f"{self.__base_url}/{id}"
            response = self.__get_response(url)
            return Beer(**response[0])
        except HTTPError as error:
            raise InvalidIdException(error)

    @log_if_requested
    def get_random_beer(self) -> Beer:
        url = f"{self.__base_url}/random"
        response = self.__get_response(url)
        return Beer(**response[0])

    @log_if_requested
    def get_all_beers(
        self,
        page: IntOrString = None,
        per_page: IntOrString = 25,
        limit: IntOrString = None,
    ) -> Beers:
        # Get beers from the API
        # Output: beers - list
        if not per_page:
            raise ArgumentsException("Per_page must be greater than 0!")

        if page in [0, "0"]:
            raise ArgumentsException("Page must be greater than 0!")

        limit = limit or per_page if page is not None else limit
        per_page = 80 if page in [1, None, "1"] else per_page
        page = page or 1

        response = []
        # response = self.__get_response(params={"page": page, "per_page": per_page})
        while (limit is None) or (len(response) < limit):
            resp = self.__get_response(params={"page": page, "per_page": per_page})
            response += resp
            page += 1
            if len(resp) < per_page:
                break

        beers = []
        for beer_details in response[:limit]:
            beers.append(Beer(**beer_details))
        return beers

    # Generator peste care pot sa iterez : get_iter_all_bears
    def get_iter_all_beers(self) -> Beer:
        beers = self.get_all_beers()
        for beer in beers:
            yield beer

    @log_if_requested
    def get_beers_brewd_before(self, month: int = None, year: int = None) -> Beers:
        # Get beers brewed before (month-year)
        response = self.__get_response(params={"brewed_before": f"{month}-{year}"})
        beers = []
        for beer_details in response:
            beers.append(Beer(**beer_details))
        return beers
