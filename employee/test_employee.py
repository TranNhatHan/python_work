from employee import Employee
import pytest # type: ignore

# def test_give_default_raise():
#     employee = Employee("Hana", "Tran", 10000)
#     employee.give_raise()
#     assert 15000 == employee.annual_salary

# def test_give_custom_raise():
#     employee = Employee("Hana", "Tran", 10000)
#     employee.give_raise(3000)
#     assert 13000 == employee.annual_salary

@pytest.fixture
def employee():
    return Employee("Hana", "Tran", 10000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert 15000 == employee.annual_salary

def test_give_custom_raise(employee):
    employee.give_raise(3000)
    assert 13000 == employee.annual_salary