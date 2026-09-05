class SmartThermostat:

    # Class-level constants
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    def __init__(self, appliance_name, initial_temp):

        # Private attribute
        self.__appliance_name = appliance_name

        # Check initial temperature
        if self.MIN_TEMP <= initial_temp <= self.MAX_TEMP:
            self.__target_temp = float(initial_temp)
        else:
            self.__target_temp = 22.0

    # Read-only property for appliance name
    @property
    def appliance_name(self):
        return self.__appliance_name

    # Getter for target temperature
    @property
    def target_temp(self):
        return self.__target_temp

    # Setter for target temperature
    @target_temp.setter
    def target_temp(self, new_temp):

        if self.MIN_TEMP <= new_temp <= self.MAX_TEMP:
            self.__target_temp = float(new_temp)

        else:
            raise ValueError(
                "Temperature must be between 10.0 and 35.0 degrees."
            )


# ---------------- TESTING ----------------

thermostat = SmartThermostat("Living Room AC", 24.0)

print("Appliance Name:", thermostat.appliance_name)
print("Target Temperature:", thermostat.target_temp)


# Update temperature
thermostat.target_temp = 28.0

print("\nUpdated Temperature:", thermostat.target_temp)


# Invalid temperature
try:
    thermostat.target_temp = 5.0

except ValueError as e:
    print("\nError:", e)