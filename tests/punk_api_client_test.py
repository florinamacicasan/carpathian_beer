from client.punk_api_base_session import PunkAPIBaseSession


class DummySession(PunkAPIBaseSession):
    def get(self):
        return []
