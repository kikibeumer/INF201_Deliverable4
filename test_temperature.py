from task1_code import Temperature
import pytest

# test_temperature.py

import pytest
from temperature import Temperature


def test_default_unit_is_celsius():
    """Temperature should default to Celsius."""
    temp = Temperature(25)

    assert temp.unit == "C"


@pytest.mark.parametrize("unit", ["c", "C", "f", "F", "k", "K"])
def test_units_are_case_insensitive(unit):
    """Units should be accepted regardless of case."""
    temp = Temperature(25, unit)

    assert temp.unit == unit.upper()


def test_unit_is_read_only():
    """The unit attribute should not be modifiable."""
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.unit = "F"


def test_value_is_read_only():
    """The temperature value should not be modifiable."""
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 30
