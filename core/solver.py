from core.tasks import solver_task
from langchain.prompts import PromptTemplate
from core.plan import Plan
from core.state import ReWOO
from typing import List
from langchain.chains.llm import LLMChain
from langchain_core.output_parsers.string import StrOutputParser


def solver_agent(state: ReWOO) -> ReWOO:

    state["generation"] = state["solver"].invoke(state["query"],state["planner"].plans)

    return state


class Solver:

    def __init__(self, llm, prompt: PromptTemplate = solver_task()) -> None:
        self._llm = llm
        self._prompt = prompt
        self._generation = None

    @property
    def generation(self) -> str:
        return self._generation

    def invoke(self, query: str, plans: List[Plan]):

        llm_chain = LLMChain(
            prompt=self._prompt, llm=self._llm, output_parser=StrOutputParser()
        )

        self._generation = llm_chain.invoke(
            {
                "query": query,
                "context": self.build_context(plans)
            }
        )

        return self.generation

    @classmethod
    def build_context(self, plans: List[Plan]):
        return "\n".join(
            [f'Plan: {plan["description"]}\nEvidence: {plan["evidence"]}\n' for plan in plans.values()]
        )
