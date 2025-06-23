from file_io_manager import FileIOManager
from job_sorter import JobSorter
from parameter_manager import ParameterManager
from task_generator import TaskGenerator

if __name__ == "__main__":
    # parameter = ParameterManager.get_user_parameters(4, 1, 10, 5, 20, 1, 10, 2, 7, 50)
    # FileIOManager.save_to_json(parameter, "param.json")
    # loaded_params  = FileIOManager.load_from_json("param.json")
    #
    # tasks = TaskGenerator.generate_tasks(loaded_params)
    # jobs = TaskGenerator.generate_jobs(tasks, loaded_params["T"])
    # FileIOManager.save_to_json(jobs, "jobs1.json")

    loaded_jobs = FileIOManager.load_from_json("jobs1.json")
    sorted_job = JobSorter.sort_by_release_time(loaded_jobs)
    print(sorted_job)
