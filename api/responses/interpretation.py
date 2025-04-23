
from typing import NotRequired, TypedDict

from api.responses.item import Item

class Interpretation(TypedDict):
    uri: str
    language: str
    longTitle: NotRequired[str]
    shortTitle: NotRequired[str]
    orderTitle: NotRequired[str]
    original: bool
    current: bool
    item: NotRequired[Item]
