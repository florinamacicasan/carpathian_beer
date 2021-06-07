import logging

from carpathian_beer import Client

#TODO: move loggin
logging.basicConfig(filename="runner.log", filemode="w", level=logging.DEBUG)


def main() -> None:
    logging.info("Start")
    client = Client()
    print(client.get_beer("1"))
    print(client.get_random_beer())
    # print(client.get_all_beers())
    logging.info("End")


if __name__ == "__main__":
    main()
