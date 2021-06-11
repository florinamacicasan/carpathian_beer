from carpathian_beer import Client
import pprint
import argparse
from dataclasses import asdict
import sys
from typing import Any


def make_client(args: Any) -> Client:
    if args.log_to_stdout:
        client = Client(file_logger=args.file_logger, log_to_stdout=True)
    else:
        client = Client(file_logger=args.file_logger, log_to_stdout=False)
    return client


def fetch_beer_by_id(args: Any) -> None:
    client = make_client(args)
    if args.id:
        id = int(args.id)
        beer = client.get_beer(id)
        pprint.pprint(asdict(beer))
    else:
        pprint.pprint("Specify id argument !")


def fetch_random_beer(args: Any) -> None:
    client = make_client(args)
    beer = client.get_random_beer()
    pprint.pprint(asdict(beer))


def fetch_beers(args: Any) -> None:
    client = make_client(args)
    arg = {}
    if args.page or args.page in [0, "0"]:
        arg["page"] = int(args.page)

    if args.per_page or args.per_page in [0, "0"]:
        arg["per_page"] = int(args.per_page)

    if args.limit or args.limit in [0, "0"]:
        arg["limit"] = int(args.limit)

    beers = client.get_all_beers(**arg)
    beers_list = []
    for beer in beers:
        beers_list.append(asdict(beer))
    pprint.pprint(beers_list)


def argparse_setup() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="carpathian_beer")
    parser.add_argument(
        "--log-to-stdout", help="specify if should log to standard output", type=bool
    )
    parser.add_argument("--file-logger", help="specify filename to log", type=str)
    parser.set_defaults(func=make_client)
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

    return parser


def carpathian_beer() -> None:
    try:
        parser = argparse_setup()
        args = parser.parse_args()
        args.func(args)
        exit(0)
    except Exception as exception:
        print(exception, file=sys.stderr)
        exit(1)
