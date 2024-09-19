"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # Label and field for Celsius
        self.addLabel(text = "Celcius", row = 0, column = 0)
        self.celc = self.addFloatField(value = 0.0, row = 1, column = 0, precision = 1)

        # Label and field for Fahrenheit
        self.addLabel(text = "Fahrenheit", row = 0, column = 1)
        self.fahr = self.addFloatField(value = 32.0, row = 1, column = 1, precision = 1)

        # Celsius to Fahrenheit button
        self.addButton(text = ">>>>", row = 3, column = 0, command = self.computeFahr)

        # Fahrenheit to Celsius button
        self.addButton(text = "<<<<", row = 3, column = 1, command = self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celc = self.celc.getNumber()
        fahr = (celc * (9/5)) + 32
        self.fahr.setNumber(fahr)


    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahr = self.fahr.getNumber()
        celc = (fahr - 32) * (5/9)
        self.celc.setNumber(celc)


def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()

