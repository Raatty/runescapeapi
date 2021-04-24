import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

import requests
from runescapeapi.runemetrics import RUNEMETRICS_BASE, SKILL_NAMES


@dataclass
class Activity:
    date: datetime
    details: str
    text: str


@dataclass
class Skill:
    name: str
    level: int
    xp: int
    rank: int
    id: int


@dataclass
class QuestsSummary:
    started: int
    complete: int
    not_started: int


@dataclass
class Profile:
    name: str
    rank: int
    total_skill: int
    total_xp: int
    combat_level: int
    magic: int
    melee: int
    ranged: int
    quests_summary: QuestsSummary
    activities: List[Activity]
    skill_values: List[Skill]
    logged_in: bool


def get_profile_url(user_name: str) -> str:
    return (
        f"{RUNEMETRICS_BASE}profile/profile?user={user_name}&activities=20"
    )


def profile_from_responce(raw_response: str) -> Profile:
    j = json.loads(raw_response)
    return Profile(
        name=j["name"],
        rank=int(j["rank"].replace(",", "")),
        total_skill=j["totalskill"],
        total_xp=j["totalxp"],
        combat_level=j["combatlevel"],
        magic=j["magic"],
        melee=j["melee"],
        ranged=j["ranged"],
        quests_summary=QuestsSummary(
            started=j["questsstarted"],
            complete=j["questscomplete"],
            not_started=j["questsnotstarted"],
        ),
        activities=[
            Activity(
                date=datetime.strptime(act["date"], "%d-%b-%Y %H:%M"),
                details=act["details"],
                text=act["text"],
            )
            for act in j["activities"]
        ],
        skill_values=[
            Skill(
                name=SKILL_NAMES[skill["id"]],
                level=skill["level"],
                xp=skill["xp"] / 10,
                rank=skill["rank"],
                id=skill["id"],
            )
            for skill in j["skillvalues"]
        ],
        logged_in=j["loggedIn"],
    )


def try_fetch_rune_metrics_profile(user_name: str) -> Profile:
    r = requests.get(get_profile_url(user_name)).text
    return profile_from_responce(r)
