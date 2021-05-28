from carpathian_beer.client.punk_api_client import PunkApiClient

def main():
    client = PunkApiClient()
    for beer  in client.get_iter_all_beers():
        print(beer)


main()