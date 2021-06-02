class Beer:
    # Dataclass - refactorizare! imutable

    def __init__(self, beer_details):
        self.__beer_details = beer_details

    @property
    def id(self):
        return self.__beer_details["id"]

    @property
    def name(self):
        return self.__beer_details["name"]

    @property
    def ingredients(self):
        return self.__beer_details["ingredients"].keys()

    @property
    def brewers_tips(self):
        return self.__beer_details["brewers_tips"]

    @property
    def first_brewed(self):
        return self.__beer_details["first_brewed"]

    @property
    def description(self):
        return self.__beer_details["description"]

    @property
    def food_pairing(self):
        return self.__beer_details["food_pairing"]

    def __repr__(self):
        return f"instance of <Beer> {self.name} "
