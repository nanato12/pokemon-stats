from typing import List, Union
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from ..consts import Config
from ..objects import Pokemon


class ScrapStats:
    pokemons: List[Pokemon]

    def __init__(self) -> None:
        res = requests.get(urljoin(Config.HOST, Config.PATH_STATS_LIST))
        self.soup = BeautifulSoup(res.content, "html.parser")
        self._get()

    def _get(self) -> None:
        self.pokemons = []

        tbody: Tag = self.soup.find("tbody")

        for tr in tbody.find_all("tr"):
            td_texts: List[str] = [td.text for td in tr.find_all("td")]

            data: List[Union[str, int]] = []
            for text in td_texts:
                if text.isdecimal():
                    data.append(int(text))
                else:
                    data.append(text)

            self.pokemons.append(Pokemon(*data))
