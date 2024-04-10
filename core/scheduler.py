import re
from typing import List
from core.plan import Plan


class Executor:
    def __init__(self) -> None:
        self._tools_map = None

    def set_space(self, tools):
        self._tools_map = {tool.name: tool for tool in tools}

    def execute(self, plans: List[Plan]):
        for plan in plans.values():
            args = plan["args"]
            for idx in re.findall(r"#E\d+", args):
                if "evidence" in plans[idx]:
                    args = args.replace(idx, plans[idx]["evidence"])
            plan["evidence"] = str(self._tools_map[plan["tool_name"]].invoke(args))
