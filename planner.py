from groq import Groq
from models import Task

import json
import re



SYSTEM_PROMPT = """
You are an LLM Compiler planner.

Always use the available tools to 
look up current product information
and pricing. And always use the available 
tools to look up popular places in 
countries. do not rely on general
knowledge about coffee and do not 
rely on general knowledge about places


Return ONLY valid JSON.

Available tools:
- get_popular_places
- get_product_info
- get_cheapest_product
- final_answer

Example:

[
  {
    "id": 1,
    "tool": "get_popular_places",
    "args": "France",
    "depends_on": []
  }
]

Always create a final_answer task.

The final_answer task depends on all previous tasks.

Use placeholders:
$1
$2
$3

Return ONLY JSON.


"""

class Planner:

    def __init__(self, _):

        self.client = Groq()

    def create_plan(self, user_input):
        
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        text = response.choices[0].message.content

        json_match = re.search(
            r"\[.*\]",
            text,
            re.DOTALL
        )

        tasks_json = json.loads(
            json_match.group()
        )

        tasks = []

        for t in tasks_json:
            tasks.append(
                Task(
                    id=t["id"],
                    tool=t["tool"],
                    args=t["args"],
                    depends_on=t["depends_on"]
                )
            )

        return tasks