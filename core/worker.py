from core.state import ReWOO  
from core.plan import Plan
from typing import List
from core.scheduler import Executor

def worker_agent(state: ReWOO):

    worker = Worker(state["tools"])
    worker.invoke(state["planner"].plans)

    return state

class Worker:

    def __init__(self, tools) -> None:
        self.scheduler = Executor(tools)

    def invoke(self, plans: List[Plan]):
        self.scheduler.execute(plans)
