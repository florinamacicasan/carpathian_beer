from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Beer:
    id: int
    name: str
    tagline: str
    first_brewed: str
    description: str
    image_url: str
    abv: float
    ibu: int
    target_fg: int
    target_og: int
    ebc: int
    srm: int
    ph: float
    attenuation_level: int
    volume: dict
    boil_volume: dict
    method: dict
    ingredients: dict
    food_pairing: list
    brewers_tips: str
    contributed_by: str
