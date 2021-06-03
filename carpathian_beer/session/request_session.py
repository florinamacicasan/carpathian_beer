import requests

from carpathian_beer.session.punk_api_base_session import PunkAPIBaseSession


class RequestSession(PunkAPIBaseSession):
    def __init__(self):
        self._session = requests.Session()

    def get(self, url, parameters=None):
        if parameters:
            return self._session.get(url, params=parameters)
        return self._session.get(url)
