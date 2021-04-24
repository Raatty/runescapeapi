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


def get_quests_url(user_name: str) -> str:
    return f"{RUNEMETRICS_BASE}quests?user={user_name}"


def quests_from_response(raw_response: str) -> List[Quest]:
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


def try_fetch_quests_list(user_name: str) -> List[Quest]:
    r = requests.get(get_quests_url(user_name)).text
    return quests_from_response(r)
