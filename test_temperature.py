from temperature import Temperature
import pytest


# 1. Initialization: Default unit, case-insensitive units, and read-only behavior.

def test_default_unit_is_celsius():
    """Test that the default unit is Celsius when not specified."""
    temp = Temperature(25)

    # Check that the default unit is 'C' and the value is correctly set.
    assert temp.unit == "C"
    assert temp.value == 25.0


@pytest.mark.parametrize("unit", ["c", "C", "f", "F", "k", "K"])
def test_units_are_case_insensitive(unit):
    """Test that the unit is case-insensitive and is stored in uppercase."""
    temp = Temperature(25, unit)

    # Check that the unit is stored in uppercase and the value is correctly set.
    assert temp.unit == unit.upper()


def test_unit_is_read_only():
    """Test that the unit attribute is read-only."""
    temp = Temperature(25, "C")

    # Attempting to change the unit should raise an AttributeError.
    with pytest.raises(AttributeError):
        temp.unit = "F"


def test_value_is_read_only():
    """Test that the value attribute is read-only."""
    temp = Temperature(25, "C")

    # Attempting to change the value should raise an AttributeError.
    with pytest.raises(AttributeError):
        temp.value = 30


# 2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".

@pytest.mark.parametrize("unit", ["X", "", "CELSIUS"])
def test_invalid_units(unit):
    """Test that invalid unit strings raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, unit)


def test_below_absolute_zero_celsius():
    """Test that temperatures below absolute zero in Celsius raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(-274, "C")


def test_below_absolute_zero_fahrenheit():
    """Test that temperatures below absolute zero in Fahrenheit raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(-500, "F")


def test_below_absolute_zero_kelvin():
    """Test that temperatures below absolute zero in Kelvin raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(-1, "K")


def test_invalid_target_unit():
    """Test that converting to an invalid target unit raises a ValueError."""
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to("X")


# 3. Conversion Accuracy: Test conversion accuracy across reference points

def test_absolute_zero():
    """Test conversion accuracy at absolute zero."""
    temp = Temperature(0, "K")

    # Check that absolute zero in Kelvin converts correctly to Celsius and Fahrenheit.
    assert temp.to_celsius() == pytest.approx(-273.15)
    assert temp.to_fahrenheit() == pytest.approx(-459.67)


def test_celsius_fahrenheit_crossover():
    """Test conversion accuracy at the crossover point between Celsius and Fahrenheit."""
    temp = Temperature(-40, "C")

    # Check that -40°C converts correctly to Fahrenheit.
    assert temp.to_fahrenheit() == pytest.approx(-40)


def test_freezing_point_of_water():
    """Test conversion accuracy at the freezing point of water."""
    temp = Temperature(0, "C")

    # Check that the freezing point of water in Celsius converts correctly to Fahrenheit and Kelvin.
    assert temp.to_fahrenheit() == pytest.approx(32)
    assert temp.to_kelvin() == pytest.approx(273.15)


def test_human_body_temperature():
    """Test conversion accuracy at human body temperature."""
    temp = Temperature(37, "C")

    # Check that human body temperature in Celsius converts correctly to Fahrenheit and Kelvin.
    assert temp.to_fahrenheit() == pytest.approx(98.6)
    assert temp.to_kelvin() == pytest.approx(310.15)


def test_boiling_point_of_water():
    """Test conversion accuracy at the boiling point of water."""
    temp = Temperature(100, "C")

    # Check that the boiling point of water in Celsius converts correctly to Fahrenheit and Kelvin.
    assert temp.to_fahrenheit() == pytest.approx(212)
    assert temp.to_kelvin() == pytest.approx(373.15)


# 4. Round-trip Conversion: Converting "C" -> "F" -> "K" -> "C" reproduces the original Temperature

def test_round_trip_conversion():
    """Test that converting from Celsius to Fahrenheit to Kelvin and back to Celsius reproduces the original temperature."""
    original = Temperature(25, "C")

    # Perform the round-trip conversion: C -> F -> K -> C
    converted = (original
        .convert_to("F")
        .convert_to("K")
        .convert_to("C"))

    # Check that the final converted temperature is equal to the original temperature.
    assert converted == original


# 5. Cross-Unit Comparisons: Equality and ordering (<, <=, >, >=) across mixed units

def test_cross_unit_equality():
    """Test that temperatures in different units can be compared for equality."""
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(100, "C") == Temperature(212, "F")
    assert Temperature(273.15, "K") == Temperature(0, "C")


def test_cross_unit_ordering():
    """Test that temperatures in different units can be compared for ordering."""
    assert Temperature(0, "C") < Temperature(100, "C")
    assert Temperature(32, "F") <= Temperature(0, "C")
    assert Temperature(100, "C") > Temperature(273.15, "K")
    assert Temperature(100, "C") >= Temperature(212, "F")


def test_comparison_with_non_temperature():
    """Test that comparing a Temperature object with a non-Temperature object returns NotImplemented."""
    assert Temperature(25, "C").__eq__(25) is NotImplemented


# 6. String Formatting: Outputs of str() and repr()

def test_str():
    """Test the string representation is formatted correctly."""
    temp = Temperature(25, "C")

    assert str(temp) == "25.00 °C"


def test_repr():
    """Test the representation is formatted correctly."""
    temp = Temperature(25.0, "C")

    assert repr(temp) == "Temperature(25.0, 'C')"