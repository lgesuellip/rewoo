from langchain_core.output_parsers.base import BaseOutputParser
from typing import List
import re
from core.plan import Plan

REGEX_PATTERN = r"Plan:\s*(.+)\s*(#E\d+)\s*=\s*(\w+)\s*\[([^\]]+)\]"


class PlannerOutputParser(BaseOutputParser):
    """
    """

    def parse(self, text: str) -> List[Plan]:
        plans = {}
        for description, idx, tool_name, args in re.findall(REGEX_PATTERN, text):
            plans[idx] = Plan(description=description, tool_name=tool_name, args=args)
        return plans
