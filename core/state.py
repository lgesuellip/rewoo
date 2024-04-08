from typing import TypedDict, List


class ReWOO(TypedDict):
    query: str
    planner: "Planner"
    tools: List[callable]
