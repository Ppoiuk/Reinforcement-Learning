import random


class JobSimulator:
    @staticmethod
    # Assign a random execution time between C_min and C_max for each job
    def assign_computation_time(jobs):
        for job in jobs:
            job["computation_time"] = random.randint(job["C_min"], job["C_max"])
        return jobs

    @staticmethod
    def simulate(jobs, T):
        current_time = 0  # Simulation clock
        executed_jobs = []  # List to store executed jobs
        remaining_jobs = jobs.copy()  # Copy of the job list to modify during simulation

        while remaining_jobs and current_time <= T:
            # Get jobs that are ready to run at the current time
            ready_jobs = [job for job in remaining_jobs if job["r"] <= current_time]

            # If there's no jobs ready, advance time by 1
            if not ready_jobs:
                current_time += 1
                continue

            # Randomly pick one of the ready jobs
            job = random.choice(ready_jobs)
            exec_time = job["computation_time"]

            # Skip this job if it cannot finish before the time limit
            if current_time + exec_time > T:
                remaining_jobs.remove(job)
                continue

            # Set the start and end time of the job
            job["start_time"] = current_time
            job["end_time"] = current_time + exec_time

            # Mark the job as executed
            executed_jobs.append(job)
            # Move the clock forward by the job's execution time
            current_time += exec_time
            # Remove the job from the list of remaining jobs
            remaining_jobs.remove(job)

        return executed_jobs
