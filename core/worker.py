from core.state import ReWOO  
from core.plan import Plan
from typing import List
from core.scheduler import Executor

def worker_agent(state: ReWOO):

    state["worker"].invoke(tools=state["tools"], plans=state["planner"].plans)

    return state


class Worker:

    def __init__(self, scheduler: Executor) -> None:
        self.scheduler = scheduler

    def invoke(self, tools: List, plans: List[Plan]):
        self.scheduler.set_space(tools)
        self.scheduler.execute(plans)
