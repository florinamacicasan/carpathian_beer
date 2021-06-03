import pytest
import responses

from carpathian_beer.exceptions.carpathian_beer_exceptions import InvalidIdException
from carpathian_beer.session.client import PunkApiClient


def get_dummy_beer(id):
    return {
        "id": id,
        "name": "Trashy Blonde",
        "first_brewed": "04/2008",
        "description": "A titillating, neurotic, peroxide punk of a Pale Ale.",
        "ingredients": {
            "malt": [
                {
                    "name": "Maris Otter Extra Pale",
                    "amount": {"value": 3.25, "unit": "kilograms"},
                },
                {
                    "name": "Caramalt",
                    "amount": {"value": 0.2, "unit": "kilograms"},
                },
                {
                    "name": "Munich",
                    "amount": {"value": 0.4, "unit": "kilograms"},
                },
            ],
            "hops": [
                {
                    "name": "Amarillo",
                    "amount": {"value": 13.8, "unit": "grams"},
                    "add": "start",
                    "attribute": "bitter",
                },
                {
                    "name": "Simcoe",
                    "amount": {"value": 13.8, "unit": "grams"},
                    "add": "start",
                    "attribute": "bitter",
                },
                {
                    "name": "Amarillo",
                    "amount": {"value": 26.3, "unit": "grams"},
                    "add": "end",
                    "attribute": "flavour",
                },
                {
                    "name": "Motueka",
                    "amount": {"value": 18.8, "unit": "grams"},
                    "add": "end",
                    "attribute": "flavour",
                },
            ],
            "yeast": "Wyeast 1056 - American Ale™",
        },
        "food_pairing": [
            "Fresh crab with lemon",
            "Garlic butter dipping sauce",
            "Goats cheese salad",
            "Creamy lemon bar doused in powdered sugar",
        ],
        "brewers_tips": "Be careful not to collect too much wort from the mash",
    }


# Generator peste care pot sa iterez
def generate_beers(ids):
    for id in ids:
        beer = get_dummy_beer(id)
        yield beer


CLIENT = PunkApiClient()


@responses.activate
def test_get_beer():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers/2",
        json=list(generate_beers([2])),
        status=200,
    )

    assert CLIENT.get_beer(2).id == 2


@responses.activate
def test_get_beer_invalid_id():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers/a",
        json=list(generate_beers(["a"])),
        status=400,
    )

    with pytest.raises(InvalidIdException):
        CLIENT.get_beer("a")


@responses.activate
def test_get_random_beer():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers/random",
        json=list(generate_beers([2])),
        status=200,
    )

    assert CLIENT.get_random_beer().id == 2


@responses.activate
def test_get_all_beers_from_page():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=2&per_page=25",
        json=list(generate_beers(range(26, 51))),
        status=200,
    )

    assert len(CLIENT.get_all_beers(page=2)) == 25


@responses.activate
def test_get_all_beers_limit():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=3&per_page=25",
        json=list(generate_beers(range(51, 76))),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=4&per_page=25",
        json=list(generate_beers(range(76, 101))),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=5&per_page=25",
        json=list(generate_beers(range(101, 126))),
        status=200,
    )

    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=6&per_page=25",
        json=list(generate_beers(range(126, 151))),
        status=200,
    )

    assert len(CLIENT.get_all_beers(page=3, limit=90)) == 90


@responses.activate
def test_get_all_beers_per_page():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=2&per_page=10",
        json=list(generate_beers(range(11, 21))),
        status=200,
    )

    assert (len(CLIENT.get_all_beers(page=2, per_page=10))) == 10


@responses.activate
def test_get_beers_brewd_before():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?brewed_before=11-2015",
        json=list(generate_beers(range(1, 21))),
        status=200,
    )

    assert (len(CLIENT.get_beers_brewd_before(month=11, year=2015))) == 20


def test_iter_all_beers():
    responses.add(
        responses.GET,
        "https://api.punkapi.com/v2/beers?page=1&per_page=80",
        json=list(generate_beers(range(1, 81))),
        status=200,
    )
    beer_generator = CLIENT.get_iter_all_beers()
    assert next(beer_generator).id == 1
