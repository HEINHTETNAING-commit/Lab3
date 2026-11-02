from Lab2.bmi import calculate_bmi


def test_bmi_normal_weight():
    assert calculate_bmi(1.73, 57) == 0


def test_bmi_over_weight():
    assert calculate_bmi(1.70, 80) == 1


def test_bmi_under_weight():
    assert calculate_bmi(1.75, 50) == -1