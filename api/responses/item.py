
from typing import List, NotRequired, Optional, TypedDict

class Item(TypedDict):
    uri: str
    type: str
    year: int
    session: NotRequired[str]
    number: int
    title: str
    welshTitle: NotRequired[str]
    citation: str
    fullCitation: str
    commentaryCitation: str
    welshCitation: NotRequired[str]
    welshFullCitation: NotRequired[str]
    welshCommentaryCitation: NotRequired[str]
    originalLanguages: List[str]
    parent: NotRequired[str]
    children: NotRequired[List[str]]
    interpretations: NotRequired[List[str]]


class Meta:
    type: str
    year: Optional[int]
    page: int
    pageSize: int


class PageOfItems(TypedDict):
    meta: Meta
    items: List[Item]