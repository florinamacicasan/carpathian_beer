from carpathian_beer import Client
import pprint
import argparse

CLIENT = Client()
PP = pprint.PrettyPrinter(indent=4, compact=True)


def fetch_beer_by_id(args):
    if args.id:
        id = int(args.id)
        beer = CLIENT.get_beer(id)
        pprint.pprint(beer.__repr__())
    else:
        pprint.pprint("Specify id argument !")


def fetch_random_beer(args):
    beer = CLIENT.get_random_beer()
    pprint.pprint(beer)


def fetch_beers(args):
    if args.page:
        args.page = int(args.page)

    if args.per_page:
        args.per_page = int(args.per_page)

    if args.limit:
        args.limit = int(args.limit)

    beers = CLIENT.get_all_beers(args.page, args.per_page, args.limit)
    for beer in beers:
        pprint.pprint(beer)


def carpathian_beer():
    parser = argparse.ArgumentParser(prog="carpathian_beer")

    subparsers = parser.add_subparsers(help="Possible commands")

    parser_get_beer = subparsers.add_parser("get_beer", help="Fetch beer with given id")
    parser_get_beer.add_argument("id", type=int, help="id is a required int argument")
    parser_get_beer.set_defaults(func=fetch_beer_by_id)

    parser_random_beer = subparsers.add_parser(
        "get_random_beer", help="Fetch random beer"
    )
    parser_random_beer.set_defaults(func=fetch_random_beer)

    parser_get_beers = subparsers.add_parser("get_beers", help="Fetch beers")
    parser_get_beers.add_argument(
        "--page",
        help="Integer argument, specify the page to fetch beers from",
        type=int,
    )
    parser_get_beers.add_argument(
        "--per_page",
        help=" Integer argument, specify the number of beers from each page",
        type=int,
    )
    parser_get_beers.add_argument(
        "--limit",
        help="Integer argument, specify the number of beers to be display",
        type=str,
    )
    parser_get_beers.set_defaults(func=fetch_beers)

    args = parser.parse_args()
    args.func(args)
