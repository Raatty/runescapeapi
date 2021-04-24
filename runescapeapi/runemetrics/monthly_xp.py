import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

import requests
from runescapeapi.runemetrics import RUNEMETRICS_BASE, SKILL_NAMES


@dataclass
class MonthData:
    xp_gain: int
    timestamp: datetime
    rank: int


@dataclass
class MonthlyXpGain:
    skill_id: int
    total_xp: int
    average_xp_gain: int
    total_gain: int
    month_data: List[MonthData]


def get_monthly_xp_gain_url(user_name: str, skill: str) -> str:
    return (
        f"{RUNEMETRICS_BASE}xp-monthly?searchName={user_name}"
        f"&skillid={SKILL_NAMES.index(skill)}"
    )


def monthly_xp_gain_from_responce(raw_response: str) -> MonthlyXpGain:
    j = json.loads(raw_response)["monthlyXpGain"][0]
    return MonthlyXpGain(
        skill_id=j["skillId"],
        total_xp=j["totalXp"],
        average_xp_gain=j["averageXpGain"],
        total_gain=j["totalGain"],
        month_data=[
            MonthData(
                xp_gain=month["xpGain"],
                timestamp=datetime.fromtimestamp(month["timestamp"] // 1000),
                rank=month["rank"],
            )
            for month in j["monthData"]
        ],
    )


def try_fetch_monthly_xp_gain(user_name: str, skill: str) -> MonthlyXpGain:
    r = requests.get(get_monthly_xp_gain_url(user_name, skill)).text
    return monthly_xp_gain_from_responce(r)
