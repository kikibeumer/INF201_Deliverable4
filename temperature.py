class Temperature:
    """A class to represent temperature in Celsius, Kelvin, and Fahrenheit."""

    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str) -> None:
        """Initializes a Temperature object.
        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ('C', 'F', or 'K').
        """

        unit = unit.upper()

        # Validate the unit and value
        if value < 0 or unit not in ['C', 'F', 'K']:
            raise ValueError('Temperature value must be positive and unit must be C, F, or K.')

        self._value = value
        self._unit = unit

    def to_celsius(self) -> 'Temperature':
        """Converts the temperature to Celsius."""

        # If the current unit is Celsius, return a new Temperature object with the same value and unit.
        if self._unit == 'C':
            return Temperature(self._value, 'C')
        
        # If the current unit is Fahrenheit, convert to Celsius using the formula: (F - 32) * 5/9.
        elif self._unit == 'F':
            celsius_value = (self._value - 32) * 5 / 9
            return Temperature(celsius_value, 'C')

        # If the current unit is Kelvin, convert to Celsius using the formula: K - 273.15.
        elif self._unit == 'K':
            celsius_value = self._value - 273.15
            return Temperature(celsius_value, 'C')

    def to_fahrenheit(self) -> 'Temperature':
        """Converts the temperature to Fahrenheit."""

        # If the current unit is Celsius, convert to Fahrenheit using the formula: (C * 9/5) + 32.
        if self._unit == 'C':
            fahrenheit_value = (self._value * 9 / 5) + 32
            return Temperature(fahrenheit_value, 'F')

        # If the current unit is Fahrenheit, return a new Temperature object with the same value and unit.
        elif self._unit == 'F':
            return Temperature(self._value, 'F')

        # If the current unit is Kelvin, convert to Fahrenheit using the formula: (K - 273.15) * 9/5 + 32.
        elif self._unit == 'K':
            fahrenheit_value = (self._value - 273.15) * 9 / 5 + 32
            return Temperature(fahrenheit_value, 'F')

    def to_kelvin(self) -> 'Temperature':
        """Converts the temperature to Kelvin."""

        # If the current unit is Celsius, convert to Kelvin using the formula: C + 273.15.
        if self._unit == 'C':
            kelvin_value = self._value + 273.15
            return Temperature(kelvin_value, 'K')

        # If the current unit is Fahrenheit, convert to Kelvin using the formula: (F - 32) * 5/9 + 273.15.
        elif self._unit == 'F':
            kelvin_value = (self._value - 32) * 5 / 9 + 273.15
            return Temperature(kelvin_value, 'K')

        # If the current unit is Kelvin, return a new Temperature object with the same value and unit.
        elif self._unit == 'K':
            return Temperature(self._value, 'K')

    def convert_to(self, target_unit: str) -> 'Temperature':
        """Converts the temperature to the target unit."""

        target_unit = target_unit.upper()

        # Validate the target unit
        if target_unit not in ['C', 'F', 'K']:
            raise ValueError('Target unit must be C, F, or K.')

        # If the current unit is the same as the target unit, return a new Temperature object with the same value and unit.
        if self._unit == target_unit:
            return Temperature(self._value, self._unit)

        # Convert to the target unit using the appropriate conversion method.
        if target_unit == 'C':
            return Temperature(self.to_celsius(), "C")
        elif target_unit == 'F':
            return Temperature(self.to_fahrenheit(), "F")
        elif target_unit == 'K':
            return Temperature(self.to_kelvin(), "K")

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
        return f"Temperature: {self._value:.2f} {self._unit}"

    @property
    def value(self) -> float:
        """Public read-only property to inspect the temperature value without allowing direct, unsafe edits."""
        return self._value

    @property
    def unit(self) -> str:
        """Public read-only property to inspect the temperature unit without allowing direct, unsafe edits."""
        return self._unit
