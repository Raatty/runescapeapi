import json
from dataclasses import dataclass
from typing import Dict, List

import requests

from runescapeapi import BASE_URL

AREA_NAMES_URL: str = f"{BASE_URL}m=itemdb_rs/bestiary/areaNames.json"
"""
returns data like `List[str]` of area names compatable with `AreaBeasts`
"""
SLAYER_CAT_NAMES: str = f"{BASE_URL}m=itemdb_rs/bestiary/slayerCatNames.json"
"""
`Dict[str, int]`
"""
WEAKNESS_NAMES: str = f"{BASE_URL}m=itemdb_rs/bestiary/weaknessNames.json"
"""
`Dict[str, int]`
"""


@dataclass
class BeastData:
    name: str
    beast_id: int
    members: bool
    weakness: str
    level: int
    life_points: int
    defence: int
    attack: int
    magic: int
    ranged: int
    xp: float
    slayer_level: int
    slayer_cat: str
    size: int
    attackable: bool
    aggressive: bool
    poisonous: bool
    description: str
    areas: List[str]
    animations: Dict[str, int]

    @staticmethod
    def url(beast_id: int) -> str:
        return (
            f"{BASE_URL}m=itemdb_rs/bestiary/beastData.json?beastid={beast_id}"
        )

    @staticmethod
    def from_response(raw_responce: str) -> "BeastData":
        print(raw_responce)
        j: dict[str:str] = json.loads(raw_responce)
        j.setdefault("slayerlevel", None)
        j.setdefault("slayercat", None)
        return BeastData(
            name=j["name"],
            beast_id=j["id"],
            members=j["members"],
            weakness=j["weakness"],
            level=j["level"],
            life_points=j["lifepoints"],
            defence=j["defence"],
            attack=j["attack"],
            magic=j["magic"],
            ranged=j["ranged"],
            xp=float(j["xp"]),
            slayer_level=j["slayerlevel"],
            slayer_cat=j["slayercat"],
            size=j["size"],
            attackable=j["attackable"],
            aggressive=j["aggressive"],
            poisonous=j["poisonous"],
            description=j["description"],
            areas=j["areas"],
            animations=j["animations"],
        )

    @classmethod
    def try_fetch(cls, beast_id: int) -> "BeastData":
        url = cls.url(beast_id)
        print(url)
        r = requests.get(url).text
        print(r)
        return cls.from_response(r)


print()
print(BeastData.try_fetch(89))  # UNICORN?
