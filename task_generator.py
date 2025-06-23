import random


class TaskGenerator:
    @staticmethod
    def generate_tasks(params):
        tasks = []
        for i in range(params["m"]):
            C_min = random.randint(params["LCmin"], params["UCmax"] - 1)
            C_max = random.randint(C_min + 1, params["UCmax"])
            D = random.randint(params["LD"], params["UD"])
            p = random.randint(params["LP"], params["UP"])
            n = random.randint(params["LN"], params["UN"])

            task = {
                "task_id": f"T{i}",
                "C_min": C_min,
                "C_max": C_max,
                "Di": D,
                "priority": p,
                "n": n
            }

            tasks.append(task)
        return tasks

    @staticmethod
    def generate_jobs(tasks, T):
        jobs = []
        for task in tasks:
            for j in range(task["n"]):
                r = random.randint(0, T)
                job = {
                    "task_id": task["task_id"],
                    "r": r,
                    "C_min": task["C_min"],
                    "C_max": task["C_max"],
                    "Di": task["Di"],
                    "priority": task["priority"]
                }
                jobs.append(job)
        return jobs