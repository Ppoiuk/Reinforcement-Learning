import json
import random


def get_user_parameters(m, LCmin, UCmax, LD, UD, LP, UP, LN, UN, T):
    parameters = {
        "m": m,
        "LCmin": LCmin,
        "UCmax": UCmax,
        "LD": LD,
        "UD": UD,
        "LP": LP,
        "UP": UP,
        "LN": LN,
        "UN": UN,
        "T": T
    }
    return parameters

def save_parameters_to_json(parameters, filename):
    with open(filename, 'w') as f:
        json.dump(parameters, f, indent=4)

def load_parameters_from_json(filename):
    with open(filename, 'r') as f:
        params = json.load(f)
    return params

def generate_tasks_from_params(params):
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

def generate_jobs_for_json_output(tasks, T):
    jobs = []
    for task in tasks:
        task_id = task["task_id"]
        C_min = task["C_min"]
        C_max = task["C_max"]
        Di = task["Di"]
        priority = task["priority"]
        n = task["n"]

        for j in range(n):
            rj = random.randint(0, T)
            job = {
                "task_id": task_id,
                "rj": rj,
                "C_min": C_min,
                "C_max": C_max,
                "Di": Di,
                "priority": priority
            }
            jobs.append(job)

    return jobs

def save_jobs_to_json(jobs, filename):
    with open(filename, 'w') as f:
        json.dump(jobs, f, indent=4)

if __name__ == "__main__":

    parameters = get_user_parameters(5, 1, 10, 5, 20, 1, 10, 2, 7, 50)
    save_parameters_to_json(parameters, "parameters.json")


    loaded_params = load_parameters_from_json("parameters.json")
    tasks = generate_tasks_from_params(loaded_params)

    jobs = generate_jobs_for_json_output(tasks, loaded_params["T"])
    save_jobs_to_json(jobs, "jobs.json")

    print(tasks)