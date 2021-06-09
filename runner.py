from carpathian_beer import Client


def main() -> None:
    # logging.info("Start")
    client = Client(shouldLog=True)
    # print(client.get_beer("1"))
    # print(client.get_random_beer())
    print(client.get_all_beers())
    # logging.info("End")


if __name__ == "__main__":
    main()
