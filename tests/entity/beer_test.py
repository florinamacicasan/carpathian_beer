import logging

from carpathian_beer.entity.beer import Beer

# Test functions for Beer class methods


def test_beer_details():
    beer = Beer(
        {
            "id": 5,
            "name": "Ursus",
            "ingredients": {"malt": [], "hops": [], "yeast": []},
            "brewers_tips": "taste is all that matters",
            "first_brewed": "05/2007",
            "description": "strong and bitter taste",
            "food_pairing": ["baked beans", "roast chicken"],
        }
    )
    try:
        assert beer.id == 5
        assert beer.name == "Ursus"
        assert len(beer.ingredients) == 3
        assert beer.brewers_tips == "taste is all that matters"
        assert beer.first_brewed == "05/2007"
        assert beer.description == "strong and bitter taste"
        assert len(beer.food_pairing) == 2
        assert beer.food_pairing[1] == "roast chicken"
        logging.info("test_beer_details succeed")
    except AssertionError as exception:
        logging.error("test_beer_details failed")
        raise exception
