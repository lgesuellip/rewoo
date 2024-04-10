from typing import TypedDict, List


class ReWOO(TypedDict):
    query: str
    tools: List
    planner: "Planner"
    worker: "Worker"
    solver: "Solver"
    generation: str

