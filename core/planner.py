from core.tasks import planner_task
from core.parsers import PlannerOutputParser
from core.state import ReWOO
from core.plan import Plan
from typing import List, Optional
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from textwrap import dedent


def planner_agent(state: ReWOO) -> ReWOO:

    state["planner"].invoke(state["query"], state["tools"])

    return state

class Planner:

    def __init__(
        self, llm, few_shot: str, exemplars: Optional[str] = None, prompt: PromptTemplate = planner_task()
    ) -> None:
        self._llm = llm
        self._exemplars = exemplars
        self._few_shot = few_shot
        self._prompt = prompt
        self._plans: List[Plan] = None

    @property
    def plans(self) -> Plan:
        return self._plans

    def invoke(self, query: str, tools: List):

        if not self._exemplars:
            self._exemplars = self.generate_exemplars_prompt(tools)

        llm_chain = LLMChain(
            prompt=self._prompt, llm=self._llm, output_parser=PlannerOutputParser()
        )

        self._plans = llm_chain.invoke(
            {
                "query": query,
                "exemplars": self._exemplars,
                "few_shot": self._few_shot,
            }
        )["text"]

        # parser = PlannerOutputParser()
        # self._plans = parser.parse(
        #     text=dedent(
        #         """
        #         Plan: Use Google to search for the 2024 Australian Open winner.
        #         #E1 = Google[2024 Australian Open winner]
        #         Plan: Retrieve the name of the 2024 Australian Open winner from the search results.
        #         #E2 = LLM[What is the name of the 2024 Australian Open winner, given #E1]
        #         Plan: Use Google to search for the hometown of the 2024 Australian Open winner.
        #         #E3 = Google[hometown of 2024 Australian Open winner, given #E2]
        #         Plan: Retrieve the hometown of the 2024 Australian Open winner from the search results.
        #         #E4 = LLM[What is the hometown of the 2024 Australian Open winner, given #E3]
        #         """
        #     )
        # )

    @classmethod
    def generate_exemplars_prompt(cls, tools: List):
        return "\n\n".join(
            f"{tool.name}[input]: {tool.description}\n" for tool in tools
        )
