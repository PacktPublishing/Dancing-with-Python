from enum import Enum


class MusicalInstrument:
    def __init__(self, brand, model, year_built):
        self._brand = brand
        self._model = model
        self._year_built = year_built

    def __str__(self):
        return f"{self._year_built} " \
            + f"{self._brand} {self._model}"


class Guitar(MusicalInstrument):
    def __init__(self, brand, model, year_built, strings=6):
        super().__init__(brand, model, year_built)
        self._strings = strings

    def __str__(self):
        return f"{self._strings}-string " \
            + super().__str__()


class Pickup(Enum):
    UNKNOWN = "unknown"
    SINGLECOIL = "single coil"
    HUMBUCKER = "Humbucker"
    ACTIVE = "active"
    GOLDFOIL = "gold foil"
    TOASTER = "toaster"


class ElectricGuitar(Guitar):
    def __init__(self, brand, model, year_built, strings=6):
        super().__init__(brand, model, year_built, strings)
        self._pickup = Pickup.UNKNOWN

    def __str__(self):
        return f"{self._strings}-string " \
            + f"{self._year_built} " \
            + f"{self._brand} {self._model} " \
            + f"with {self._pickup.value} pickup"

    @property
    def pickup(self):
        return self._pickup

    @pickup.setter
    def pickup(self, value):
        if not isinstance(value, Pickup):
            raise ValueError("The pickup must be of "
                             "enumeration type Pickup.")
        self._pickup = value


class Clarinet(MusicalInstrument):
    pass
