import pytest
import responses

from carpathian_beer import Client
from carpathian_beer import InvalidIdException


def get_dummy_beer(id):
    return {
        "id": id,
        "name": "Ursus",
        "tagline": "ok",
        "first_brewed": "05/2007",
        "description": "strong and bitter taste",
        "image_url": "https://images.punkapi.com/v2/5.png",
        "abv": 4.5,
        "ibu": 59,
        "target_fg": 1027,
        "target_og": 1069,
        "ebc": 10,
        "srm": 5,
        "ph": 4.4,
        "attenuation_level": 67,
        "volume": {"value": 20, "unit": "litres"},
        "boil_volume": {"value": 25, "unit": "litres"},
        "method": {"mash_temp": [], "fermentation": {}},
        "ingredients": {"malt": [], "hops": []},
        "food_pairing": ["vietnamese squid salad"],
        "brewers_tips": "ok",
        "contributed_by": "Sam Mason",
    }


# Generator peste care pot sa iterez
def generate_beers(ids):
    for id in ids:
        beer = get_dummy_beer(id)
        yield beer


CLIENT = Client()


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
def test_gell_all_beers():
    beers = list(generate_beers(range(1, 330)))
    for page in range(1, 6):
        responses.add(
            responses.GET,
            f"https://api.punkapi.com/v2/beers?page={page}&per_page=80",
            json=beers[(page - 1) * 80 : page * 80],
            status=200,
        )

    assert (len(CLIENT.get_all_beers())) == 329


@responses.activate
def test_get_beers_brewed_before():
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
