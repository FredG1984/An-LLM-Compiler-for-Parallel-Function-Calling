from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    tool: str
    args: str
    depends_on: List[int]