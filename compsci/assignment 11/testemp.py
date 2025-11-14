import pytest 
from employee import employee 

@pytest.fixture
def employee():
    employee = employee("silva", "W", 50_000)
    return employee

def testraise(employee):
    employee.getraise()
    assert employee.salary == 55_000

def custraise(employee):
    employee.give_raise(7000)
    assert employee.salary == 62_000