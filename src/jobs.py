from functools import lru_cache
import csv

@lru_cache
def read(path):
    jobs = []
    with open(path) as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            jobs.append(job)
        return jobs
