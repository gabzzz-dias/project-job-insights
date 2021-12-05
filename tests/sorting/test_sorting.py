from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-01-01"},
        {"min_salary": 3000, "max_salary": 8000, "date_posted": "2020-01-01"},
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2019-01-01"},
        {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-01-01"},
        {"min_salary": 8000, "max_salary": 6000, "date_posted": "2020-01-01"},
    ]


expected = [
    {"min_salary": 3000, "max_salary": 8000, "date_posted": "2020-01-01"},
    {"min_salary": 8000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2019-01-01"},
]


def test_sort_by_criteria(jobs):
    final = sort_by(jobs, "max_salary")
    assert final == expected
