import asyncio
from tools import TOOLS

class Executor:

    def __init__(self):

        self.results = {}

    async def execute_task(self, task):

        tool = TOOLS[task.tool]

        args = task.args

            # STRING ARGUMENTS
        if isinstance(args, str):

            for dep_id, dep_result in self.results.items():

                args = args.replace(
                    f"${dep_id}",
                    str(dep_result)
                )

        # LIST ARGUMENTS
        elif isinstance(args, list):

            new_args = []

            for item in args:

                if isinstance(item, str):

                    for dep_id, dep_result in self.results.items():

                        item = item.replace(
                            f"$" + str(dep_id),
                            str(dep_result)
                        )

                new_args.append(item)

            args = new_args

        print(f"\nRUNNING TASK {task.id}")
        print(f"{task.tool}({args})")

        result = await asyncio.to_thread(
            tool,
            args
        )

        self.results[task.id] = result

        print(f"\nRESULT {task.id}")
        print(result)

    async def run(self, tasks):

        pending = tasks[:]

        while pending:

            ready_tasks = []

            for task in pending:

                if all(
                    dep in self.results
                    for dep in task.depends_on
                ):
                    ready_tasks.append(task)

            if not ready_tasks:
                raise Exception("Deadlock detected")

            await asyncio.gather(
                *[
                    self.execute_task(task)
                    for task in ready_tasks
                ]
            )

            for task in ready_tasks:
                pending.remove(task)

        return self.results