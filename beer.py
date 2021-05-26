class Beer:
    def __init__(self, beer_details):
        self.__beer_details = beer_details

    def get_id(self):
        return self.__beer_details["id"]

    def get_name(self):
        return self.__beer_details["name"]

    def get_ingredients(self):
        return self.__beer_details["ingredients"].keys()

    def get_brewers_tips(self):
        return self.__beer_details["brewers_tips"]

    def get_first_brewed(self):
        return self.__beer_details["first_brewed"]

    def get_description(self):
        return self.__beer_details["description"]

    def get_food_pairing(self):
        return self.__beer_details["food_pairing"]
