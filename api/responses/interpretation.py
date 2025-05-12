
from typing import List, NotRequired, Optional, TypedDict

from api.responses.item import Item

class Interpretation(TypedDict):
    uri: str
    language: str
    shortTitle: Optional[str]
    longTitle: NotRequired[str]
    original: bool
    current: bool
    parent: NotRequired[str]
    children: NotRequired[List[str]]
    item: NotRequired[Item]
