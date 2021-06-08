from carpathian_beer import Beer

# Test functions for Beer class methods


def test_beer_details():
    beer_attributes = {
        "id": 5,
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
    beer = Beer(**beer_attributes)

    assert beer.id == 5
    assert beer.name == "Ursus"
    assert beer.tagline == "ok"
    assert beer.first_brewed == "05/2007"
    assert beer.description == "strong and bitter taste"
    assert beer.image_url == "https://images.punkapi.com/v2/5.png"
    assert beer.abv == 4.5
    assert beer.ibu == 59
    assert beer.target_fg == 1027
    assert beer.target_og == 1069
    assert beer.ebc == 10
    assert beer.srm == 5
    assert beer.ph == 4.4
    assert beer.attenuation_level == 67
    assert len(beer.volume) == 2
    assert len(beer.boil_volume) == 2
    assert len(beer.method) == 2
    assert len(beer.ingredients) == 2
    assert beer.food_pairing[0] == "vietnamese squid salad"
    assert beer.brewers_tips == "ok"
    assert beer.contributed_by == "Sam Mason"
