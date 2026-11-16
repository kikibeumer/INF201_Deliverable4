

class Temperature:
    """A class to represent temperature in Celsius, Kelvin, and Fahrenheit."""

    def __init__(self, value: float, unit: str) -> None:
        """Initializes a Temperature object.
        Args:
            value (float): The temperature value.
            unit (str): The unit of the temperature ('C', 'F', or 'K').
        """

        if value < 0 or unit not in ['C', 'F', 'K']:
            raise ValueError('Temperature value must be positive and unit must be C, F, or K.')
        self._value = value
        self._unit = unit

    def to_celsius(self) -> 'Temperature':
        """Converts the temperature to Celsius."""

        if self._unit == 'C':
            return Temperature(self._value, 'C')
        elif self._unit == 'F':
            celsius_value = (self._value - 32) * 5 / 9
            return Temperature(celsius_value, 'C')
        elif self._unit == 'K':
            celsius_value = self._value - 273.15
            return Temperature(celsius_value, 'C')

    def to_fahrenheit(self) -> 'Temperature':
        """Converts the temperature to Fahrenheit."""

        if self._unit == 'C':
            fahrenheit_value = (self._value * 9 / 5) + 32
            return Temperature(fahrenheit_value, 'F')
        elif self._unit == 'F':
            return Temperature(self._value, 'F')
        elif self._unit == 'K':
            fahrenheit_value = (self._value - 273.15) * 9 / 5 + 32
            return Temperature(fahrenheit_value, 'F')

    def to_kelvin(self) -> 'Temperature':
        """Converts the temperature to Kelvin."""

        if self._unit == 'C':
            kelvin_value = self._value + 273.15
            return Temperature(kelvin_value, 'K')
        elif self._unit == 'F':
            kelvin_value = (self._value - 32) * 5 / 9 + 273.15
            return Temperature(kelvin_value, 'K')
        elif self._unit == 'K':
            return Temperature(self._value, 'K')

    def convert_to(self, target_unit: str) -> 'Temperature':
        """Converts the temperature to the target unit."""
        if target_unit not in ['C', 'F', 'K']:
            raise ValueError('Target unit must be C, F, or K.')

        if self._unit == target_unit:
            return Temperature(self._value, self._unit)

        if target_unit == 'C':
            return self.to_celsius()
        elif target_unit == 'F':
            return self.to_fahrenheit()
        elif target_unit == 'K':
            return self.to_kelvin()

    def __eq__(self, other: object) -> bool:
        """Checks if two Temperature objects are equal in value. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value == other._value

    def __lt__(self, other: object) -> bool:
        """Checks if this Temperature object is less than another Temperature object. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value < other._value

    def __le__(self, other: object) -> bool:
        """Checks if this Temperature object is less than or equal to another Temperature object. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value <= other._value

    def __gt__(self, other: object) -> bool:
        """Checks if this Temperature object is greater than another Temperature object. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value > other._value

    def __ge__(self, other: object) -> bool:
        """Checks if this Temperature object is greater than or equal to another Temperature object. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value >= other._value

    def __ne__(self, other: object) -> bool:
        """Checks if two Temperature objects are not equal in value. Comparing different units is possible."""
        if not isinstance(other, Temperature):
            return NotImplemented
        if self._unit != other._unit:
            other = other.convert_to(self._unit)
        return self._value != other._value

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
