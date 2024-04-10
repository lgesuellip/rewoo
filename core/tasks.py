"""task.py"""
from textwrap import dedent
from langchain.prompts import PromptTemplate


def planner_task() -> PromptTemplate:
    """"
    """
    return PromptTemplate(
        template=dedent("""
            For the following task, make plans that can solve the problem step-by-step. For each plan, \
            indicate which external tool together with tool input to retrieve evidence. You can store the \
            evidence into a variable #E that can be called by later tools. (Plan: , #E1, Plan: , #E2, Plan : , E3, ...)

            Tools can be one of the following:
            {exemplars}

            For example:
            {few_shot}

            Begin!
            Describe your plans with rich details. Each Plan should be followed by only one #E.

            Task: {query}
            """),
        input_variables=["exemplars", "few_shot", "query"],
    )

def solver_task() -> PromptTemplate:
    """"
    """
    return PromptTemplate(
        template=dedent("""
            Solve the following task or problem. To solve the problem, we have made step-by-step Plan and \
            retrieved corresponding Evidence to each Plan. Use them with caution since long evidence might \
            contain irrelevant information.

            {context}

            Now solve the question or task according to provided Evidence above. Respond with the answer \
            directly with no extra words.

            Task: {query}
            Response:
            """),
        input_variables=["query", "context"],
    )
