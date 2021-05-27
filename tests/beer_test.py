from client.beer import Beer

# Test functions for Beer class methods


def mock_beer():
    return Beer(
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


# SAU VARIABILA GLOBALA ????


def test_get_id():
    assert mock_beer().get_id() == 5


def test_get_name():
    assert mock_beer().get_name() == "Ursus"


def test_get_ingredients():
    assert len(mock_beer().get_ingredients()) == 3


def test_get_brewers_tips():
    assert mock_beer().get_brewers_tips() == "taste is all that matters"


def test_get_first_brewed():
    assert mock_beer().get_first_brewed() == "05/2007"


def test_get_description():
    assert mock_beer().get_description() == "strong and bitter taste"


def get_food_pairing():
    assert len(mock_beer().get_food_pairing()) == 2
    assert mock_beer().get_food_pairing()[1] == "roast chicken"
