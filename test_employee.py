import pytest
from employee import Employee

@pytest.fixture
def employee_info():
    """Holds the information needed for all tests."""
    employee_info = Employee('max', 'zaragoza', 55000)
    return employee_info

def test_give_default_raise(employee_info):
    """Tests to see if the default raise amount is added."""
    employee_info.give_raise()
    assert employee_info.annual_salary == 60000

def test_give_custom_raise(employee_info):
    """Tests to see if a custom raise amount is added."""
    employee_info.give_raise(10000)
    assert employee_info.annual_salary == 65000