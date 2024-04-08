import re
from typing import List
from core.plan import Plan


class Executor:

    def __init__(self, tools: List) -> None:
        self.tools_map = {tool.name: tool for tool in tools}

    def execute(self, plans: List[Plan]):

        for plan in plans.values():
            args = plan["args"]
            for idx in re.findall(r"#E\d+", plan["args"]):
                if "evidence" in plans[idx]:
                    args = plan["args"].replace(idx, plans[idx]["evidence"])
            plan["evidence"] = self.tools_map[plan["tool_name"]].invoke(args)
