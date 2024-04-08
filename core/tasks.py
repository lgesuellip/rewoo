"""task.py"""
from textwrap import dedent
from langchain.prompts import PromptTemplate


def planner_task() -> PromptTemplate:
    """"
    """
    return PromptTemplate(
        template=dedent("""
            For the following tasks, make plans that can solve the problem step-by-step. For each plan,
            indicate which external tool together with tool input to retrieve evidence. You can store the
            evidence into a variable #E that can be called by later tools. (Plan : , #E1, Plan : , #E2, Plan : , ...)

            Tools can be one of the following:
            {exemplars}

            {few_shot}

            Begin!
            Describe your plans with rich details. Each Plan should be followed by only one #E.

            Task: {query}
            """),
        input_variables=["exemplars", "few_shot", "query"],
    )
