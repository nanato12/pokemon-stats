from typing import List

from .objects import Pokemon
from .scraping import ScrapStats


def get_pokemon_stats() -> List[Pokemon]:
    return ScrapStats().pokemons
