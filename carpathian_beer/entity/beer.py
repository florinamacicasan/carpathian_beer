from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Beer:
    id: str
    name: str
    ingredients: list
    brewers_tips: str
    first_brewed: str
    description: str
    food_pairing: str

    def __init__(self, beer_details):
        self.id = beer_details["id"]
        self.name = beer_details["name"]
        self.ingredients = list(beer_details["ingredients"])
        self.brewers_tips = beer_details["brewers_tips"]
        self.first_brewed = beer_details["first_brewed"]
        self.description = beer_details["description"]
        self.food_pairing = beer_details["food_pairing"]

    def __repr__(self):
        return f"instance of <Beer> {self.name} "
