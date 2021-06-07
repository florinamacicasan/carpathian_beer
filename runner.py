import logging

from carpathian_beer import Client


def main() -> None:
    client = Client()
    # print(client.get_beer('a'))
    # gen = client.get_iter_all_beers()
    # print(next(gen))
    """
    for beer in client.get_iter_all_beers():
        print(beer)
    """
    # print(client.get_beers_brewd_before("?"))
    # print(client.get_all_beers(per_page=81))
    logging.basicConfig(filename="runner.log", level=logging.DEBUG)
    # encoding = "utf-8", level = logging.DEBUG, filemode='a',
    # format='%(name)s - %(levelname)s - %(message)s')
    logging.info("Start")

    logger = logging.getLogger(__name__)
    logger.error("err")
    # logging.warning("CEVA")

    # print(client.get_beer("1"))
    # print(client.get_random_beer())
    print(client.get_all_beers())


if __name__ == "__main__":
    main()
