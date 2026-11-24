class Temperature:
    """A class to represent temperature in Celsius, Kelvin, and Fahrenheit."""

    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = "C") -> None:
        """Initializes a Temperature object.
        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ('C', 'F', or 'K').
            Set default unit to Celsius to pass test_temperature.
        """

        unit = unit.upper()

        # Validate the unit and value
        if unit not in ["C", "F", "K"]:
            raise ValueError("Temperature unit must be C, F, or K.")

        if unit == "C" and value < -273.15:
            raise ValueError("Temperature below absolute zero.")

        if unit == "F" and value < -459.67:
            raise ValueError("Temperature below absolute zero.")

        if unit == "K" and value < 0:
            raise ValueError("Temperature below absolute zero.")

        self._value = value
        self._unit = unit

    def to_celsius(self) -> float:
        """Converts the temperature to Celsius and returns the value."""

        # If current unit is C, keep the value
        if self._unit == 'C':
            return self._value

        # If current unit is F, convert to C
        elif self._unit == 'F':
            return (self._value - 32) * 5 / 9

        # If current unit is K, convert to C
        elif self._unit == 'K':
            return self._value - 273.15

    def to_fahrenheit(self) -> float:
        """Converts the temperature to Fahrenheit and returns the value."""

        # If current unit is C, convert to F
        if self._unit == 'C':
            return (self._value * 9 / 5) + 32

        # If current unit is F, keep the value
        elif self._unit == 'F':
            return self._value

        # If current unit is K, convert to F
        elif self._unit == 'K':
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Converts the temperature to Kelvin and returns the value."""

        # If unit is C, convert to K
        if self._unit == 'C':
            return self._value + 273.15

        # If unit is F, convert to K
        elif self._unit == 'F':
            return (self._value - 32) * 5 / 9 + 273.15

        # If unit is K, keep the value
        elif self._unit == 'K':
            return self._value

    def convert_to(self, target_unit: str) -> 'Temperature':
        """Converts the temperature to the target unit."""

        target_unit = target_unit.upper()

        # Validate target unit
        if target_unit not in ['C', 'F', 'K']:
            raise ValueError('Target unit must be C, F, or K.')

        # If already in target unit, return a copy
        if self._unit == target_unit:
            return Temperature(self._value, self._unit)

        # Convert to requested unit
        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')

        elif target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')

        elif target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')

    def __eq__(self, other: object) -> bool:
        """Checks if two Temperature objects are equal in value. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return abs(self._value - other._value) <= self.TOLERANCE

    def __lt__(self, other: object) -> bool:
        """Checks if this Temperature object is less than another Temperature object. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value < other._value

    def __le__(self, other: object) -> bool:
        """Checks if this Temperature object is less than or equal to another Temperature object. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value <= other._value

    def __gt__(self, other: object) -> bool:
        """Checks if this Temperature object is greater than another Temperature object. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value > other._value

    def __ge__(self, other: object) -> bool:
        """Checks if this Temperature object is greater than or equal to another Temperature object. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value >= other._value

    def __ne__(self, other: object) -> bool:
        """Checks if two Temperature objects are not equal in value. Comparing different units is possible."""
        # If the other object is not a Temperature instance, return NotImplemented
        if not isinstance(other, Temperature):
            return NotImplemented

        # If the units are different, convert the other temperature to this unit for comparison.
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return abs(self._value - other._value) > self.TOLERANCE

    def __repr__(self) -> str:
        """Representation of temperature object"""
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        """String representation of temperature object formatted to two decimal places."""
        return f"{self._value:.2f} °{self._unit}"

    @property
    def value(self) -> float:
        """Public read-only property to inspect the temperature value without allowing direct, unsafe edits."""
        return self._value

    @property
    def unit(self) -> str:
        """Public read-only property to inspect the temperature unit without allowing direct, unsafe edits."""
        return self._unit
