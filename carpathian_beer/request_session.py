from typing import Dict

import requests
from carpathian_beer import BaseSession


class RequestSession(BaseSession):
    def __init__(self):
        self._session = requests.Session()

    Params = Dict[str, str]

    def get(self, url: str, parameters: Params = None) -> requests.Response:
        if parameters:
            return self._session.get(url, params=parameters)
        return self._session.get(url)
