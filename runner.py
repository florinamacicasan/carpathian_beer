from carpathian_beer.client.punk_api_client import PunkApiClient


def main():
    client = PunkApiClient()
    # print(client.get_beer('a'))
    # gen = client.get_iter_all_beers()
    # print(next(gen))
    """
    for beer in client.get_iter_all_beers():
        print(beer)
    """
    print(client.get_beers_brewd_before(13, -4))


main()