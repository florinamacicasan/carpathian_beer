import requests

from beer import Beer


class PunkApiClient:
    def __init__(self, base_url="https://api.punkapi.com/v2/beers/"):
        self.__base_url = base_url

    def get_response(self, url_option):
        response = requests.get(f"{self.__base_url}{url_option}")
        if response.status_code == 200:
            return response.json()
        raise Exception("invalid url")

    def get_random_beer(self):
        response = self.get_response("random")
        try:
            return Beer(response[0])
        except Exception as exception:
            return exception

    def get_beer_by_id(self, id):
        response = self.get_response(id)
        try:
            return Beer(response[0])
        except Exception as exception:
            return exception

    def get_all_beers(self):
        response = self.get_response("")
        beers = []
        try:
            for beer in response:
                beers.append(beer)
            return beers
        except Exception as exception:
            return exception


def main():
    client = PunkApiClient()
    print(client.get_random_beer().get_name())


main()
