
from typing import List, NotRequired, TypedDict

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
    interpretations: NotRequired[List[str]]
