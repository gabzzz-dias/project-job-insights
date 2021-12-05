from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)

    unique_jobs = set()

    for job in jobs:
        unique_jobs.add(job["job_type"])

    return unique_jobs


def filter_by_job_type(jobs, job_type):
    final = []

    for job in jobs:
        if job["job_type"] == job_type:
            final.append(job)

    return final


def get_unique_industries(path):
    industries = set()
    jobs = read(path)

    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])

    return list(industries)


def filter_by_industry(jobs, industry):
    final = []

    for job in jobs:
        if job["industry"] == industry:
            final.append(job)

    return final


def get_max_salary(path):
    jobs = read(path)
    max_salary = set()

    for job in jobs:
        if not (job["max_salary"] == "" or job["max_salary"] == "invalid"):
            max_salary.add(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = set()

    for job in jobs:
        if not (job["min_salary"] == "" or job["min_salary"] == "invalid"):
            min_salary.add(int(job["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    if (
        (min_salary == "" or max_salary == "")
        or (not type(min_salary) == "int" or not type(max_salary) == "int")
        or (min_salary > max_salary)
        or (not type(salary) == "int")
    ):
        raise ValueError

    if min_salary <= salary <= max_salary:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    final = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                final.append(job)
        except ValueError:
            pass

    return final
