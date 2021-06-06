from dataclasses import dataclass
from typing import List

import requests

from . import BASE_URL


@dataclass
class ClanMember:
    rsn: str
    rank: str
    clan_xp: int
    kills: int

    @staticmethod
    def url(clan_name: str) -> str:
        url = f"{BASE_URL}m=clan-hiscores/members_lite.ws?clanName={clan_name}"
        return url.replace(" ", "%20")

    @staticmethod
    def from_response(raw_responce: str) -> List["ClanMember"]:
        members = []
        for member in raw_responce.replace("\xa0", " ").splitlines()[1:]:
            print(member)
            rsn, rank, clan_xp, kills = member.split(",")
            members.append(
                ClanMember(
                    rsn=rsn, rank=rank, clan_xp=int(clan_xp), kills=int(kills)
                )
            )
        return members

    @classmethod
    def try_fetch(cls, clan_name: str) -> List["ClanMember"]:
        r = requests.get(cls.url(clan_name)).text
        return cls.from_response(r)
