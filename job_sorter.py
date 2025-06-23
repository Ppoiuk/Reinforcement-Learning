class JobSorter:
    @staticmethod
    def sort_by_release_time(jobs):
        return sorted(jobs, key=lambda job: job["r"])
