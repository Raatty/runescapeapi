import json
from dataclasses import dataclass
from typing import List

import requests
from runescapeapi.runemetrics import RUNEMETRICS_BASE


@dataclass
class Quest:
    title: str
    status: str
    difficulty: int
    members: bool
    quest_points: int
    user_elegible: bool

    @staticmethod
    def url(user_name: str) -> str:
        return f"{RUNEMETRICS_BASE}quests?user={user_name}"

    @staticmethod
    def from_response(raw_response: str) -> List["Quest"]:
        j = json.loads(raw_response)
        return [
            Quest(
                title=q["title"],
                status=q["status"],
                difficulty=q["difficulty"],
                members=q["members"],
                quest_points=q["questPoints"],
                user_elegible=q["userEligible"],
            )
            for q in j["quests"]
        ]

    @classmethod
    def try_fetch(cls, user_name: str) -> List["Quest"]:
        r = requests.get(cls.url(user_name)).text
        return cls.from_response(r)
