import employee_info


def test_get_employees_by_age_range():

    result = employee_info.get_employees_by_age_range(24, 35)

    assert len(result) == 3


def test_calculate_average_salary():

    result = employee_info.calculate_average_salary()

    assert result == 60166.666666666664


def test_get_employees_by_dept():

    result = employee_info.get_employees_by_dept("Sales")

    assert len(result) == 2
