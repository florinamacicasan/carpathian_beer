import click
from carpathian_beer import Client
import pprint

CLIENT = Client()
PP = pprint.PrettyPrinter(indent=4, compact=True)


def fetch_beer_by_id(id):
    if id:
        id = int(id)
        beer = CLIENT.get_beer(id)
        pprint.pprint(beer.__repr__())
    else:
        pprint.pprint("Specify id argument !")


def fetch_random_beer():
    beer = CLIENT.get_random_beer()
    pprint.pprint(beer)


def fetch_beers(page, per_page, limit):
    if page:
        page = int(page)

    if per_page:
        per_page = int(per_page)

    if limit:
        limit = int(limit)

    beers = CLIENT.get_all_beers(page, per_page, limit)
    for beer in beers:
        pprint.pprint(beer)


@click.command()
@click.argument("command", required=True)
@click.argument("id", required=False, type=int)
@click.option("--page", required=False, type=int)
@click.option("--per_page", required=False, type=int)
@click.option("--limit", required=False, type=int)
def carpathian_beer(command, id, page, per_page, limit):
    """
    3 commands: \n
        get_beer_by_id id where id is a required int argument \n
        get_random_beer \n
        get_beers \n
           --page      - Integer argument, specify the page to fetch beers from\n
           --per_page  - Integer argument, specify the number of beers from each page\n
           --limit     - Integer argument, specify the number of beers to be display\n
    """

    if command.lower() == "get_beer_by_id":
        fetch_beer_by_id(id)

    if command.lower() == "get_random_beer":
        fetch_random_beer()

    if command.lower() == "get_beers":
        fetch_beers(page, per_page, limit)
