from dataclasses import dataclass


@dataclass
class Pokemon:
    number: int
    name: str
    hp: int
    attack: int
    block: int
    contact: int
    defence: int
    speed: int
    total: int
