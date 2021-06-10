from carpathian_beer import Client


def main() -> None:
    # logging.info("Start")
    client = Client(file_logger='runner.log', log_to_stdout=True)
    # print(client.get_beer("1"))
    # print(client.get_random_beer())
    print(client.get_random_beer())
    # logging.info("End")


if __name__ == "__main__":
    main()
