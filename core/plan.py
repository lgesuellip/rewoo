from typing import TypedDict


class Plan(TypedDict):
    plan: str
    evidence: str
    tool_name: str
    args: str
