from typing import TypedDict


class Plan(TypedDict):
    description: str
    evidence: str
    tool_name: str
    args: str
