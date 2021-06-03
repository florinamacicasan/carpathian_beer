from carpathian_beer.session.client import PunkApiClient


def main():
    client = PunkApiClient()
    # print(client.get_beer('a'))
    # gen = client.get_iter_all_beers()
    # print(next(gen))
    """
    for beer in client.get_iter_all_beers():
        print(beer)
    """
    # print(client.get_beers_brewd_before("?"))
    # print(client.get_all_beers(per_page=81))
    print(client.get_beer("1"))
    print(client.get_random_beer())


main()
