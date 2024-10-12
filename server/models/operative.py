from pydantic import BaseModel
from typing import List

from models.weapon import Weapon
from models.equipment import Equipment
from models.uniqueaction import UniqueAction
from models.ability import Ability

class Operative(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    opname: str
    description: str
    M: str
    APL: str
    GA: str
    DF: str
    SV: str
    W: str
    weapons: List[Weapon]
    equipments: List[Equipment]
    uniqueactions: List[UniqueAction]
    abilities: List[Ability]