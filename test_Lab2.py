from Lab2 import Lab2



def test_calc_min_max_temperature():
    temperature_list = [10, 20, 30, 40, 50]

    result = Lab2.calc_min_max_temperature(temperature_list)

    assert result == [10, 50]


def test_calc_average_temperature():
    temperature_list = [10, 20, 30, 40, 50]

    result = Lab2.calc_average_temperature(temperature_list)

    assert result == 30


def test_calc_median_temperature():
    temperature_list = [10, 20, 30, 40, 50]

    result = Lab2.calc_median_temperature(temperature_list)

    assert result == 30