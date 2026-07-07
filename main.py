from planner import Planner
from executor import Executor
from dotenv import load_dotenv
import os
import asyncio
import time

load_dotenv()

planner = Planner(
    _=os.getenv()
)

executor = Executor()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("\n Chatbot: Goodbye!")
        break 

    print(" Chatbot: ",end="",flush=True)
    start = time.time()

    tasks = planner.create_plan(user_input)

    print("\nTASK DAG:\n")

    for t in tasks:
        print(t)

    results = asyncio.run(
        executor.run(tasks)
    )

    end = time.time()

    print("\nFINAL RESULTS:\n")

    final_result = max(results.keys())

    print("\nFINAL ANSWER:\n")

    print(results[final_result])


    print(f"\nTOTAL TIME: {end-start:.2f}s")