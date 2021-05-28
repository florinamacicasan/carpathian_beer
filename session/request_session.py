import requests
from punk_api_base_session import PunkAPIBaseSession


class RequestSession(PunkAPIBaseSession):
    def __init__(self):
        self._session = requests.Session()

    def get(self, url):
        return self._session.get(url)
