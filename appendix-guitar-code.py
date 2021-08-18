"""The guitar module implements the class hierarchy from Chapter 7.

Wooden      MusicalInstrument (ABC)
|           |
|           +-- Clarinet (ABC)
|           |
|           +-- Guitar
|               |
|               +-- ElectricGuitar
|               |
+---------------+-- AcousticGuitar
"""
from abc import ABC, abstractmethod
from enum import Enum


class MusicalInstrument(ABC):
    """Abstract base class for musical instruments.

    Parameters
    ----------
    brand : str
        Manufacturer brand name. E.g., "Fender".
    model : str
        Instrument model name. E.g., "Stratocaster".
    year_built : str
        Year the instrument was built.
    """
    def __init__(self, brand, model, year_built):
        self._brand = brand
        self._model = model
        self._year_built = year_built

    @abstractmethod
    def __str__(self):
        """Abstract method -
        creates a human-readable string representation.

        Returns
        -------
        :class:`NotImplementedType`
            NotImplemented
        """
        return NotImplemented


class Guitar(MusicalInstrument):
    """Guitar.

    Parameters
    ----------
    brand : str
        Manufacturer brand name. E.g., "Fender".
    model : str
        Instrument model name. E.g., "Stratocaster".
    year_built : str
        Year the instrument was built.
    strings : int, optional
        Number of strings. Default is 6.

    Also See
    --------
    :class"`MusicalInstrument`
    """
    def __init__(self, brand, model, year_built, strings=6):
        super().__init__(brand, model, year_built)
        self._strings = strings

    def __str__(self):
        """Creates a human-readable string representation.

        Returns
        -------
        str
            Description of the guitar.
        """
        return f"{self._strings}-string " \
            + f"{self._year_built} " \
            + f"{self._brand} {self._model}"


class Pickup(Enum):
    """Enumeration type of pickups for electric guitars.
    """
    UNKNOWN = "unknown"
    SINGLECOIL = "single coil"
    HUMBUCKER = "Humbucker"
    ACTIVE = "active"
    GOLDFOIL = "gold foil"
    TOASTER = "toaster"


class ElectricGuitar(Guitar):
    """Electric guitar.

    Parameters
    ----------
    brand : str
        Manufacturer brand name. E.g., "Fender".
    model : str
        Instrument model name. E.g., "Stratocaster".
    year_built : str
        Year the instrument was built.
    strings : int, optional
        Number of strings. Default is 6.

    Also See
    --------
    :class"`Guitar`
    """
    def __init__(self, brand, model, year_built, strings=6):
        super().__init__(brand, model, year_built, strings)
        self._pickup = Pickup.UNKNOWN

    def __str__(self):
        """Creates a human-readable string representation.

        Returns
        -------
        str
            Description of the electric guitar.
        """
        return f"{self._strings}-string " \
            + f"{self._year_built} " \
            + f"{self._brand} {self._model} " \
            + f"with {self._pickup.value} pickup"

    @property
    def pickup(self):
        """Style of pickup used in an electric guitar."""
        return self._pickup

    @pickup.setter
    def pickup(self, value):
        if not isinstance(value, Pickup):
            raise ValueError("The pickup must be of "
                             "enumeration type Pickup.")
        self._pickup = value


class Wooden:
    """Object made of wood

    Parameters
    ----------
    wood_name : str
        Name of wood species in object.
    """
    def __init__(self, wood_name):
        self._wood_name = wood_name

    def __str__(self):
        """Creates a human-readable string representation.

        Returns
        -------
        str
            Name of the wood used.
        """
        return self._wood_name


class AcousticGuitar(Guitar, Wooden):
    """Acoustic guitar.

    Parameters
    ----------
    brand : str
        Manufacturer brand name. E.g., "Fender".
    model : str
        Instrument model name. E.g., "Stratocaster".
    year_built : str
        Year the instrument was built.
    soundboard_wood : str
        Kind of wood used in the guitar soundboard.
    strings : int, optional
        Number of strings. Default is 6.

    Also See
    --------
    :class"`Guitar`
    :class"`Wooden`
    """
    def __init__(self, brand, model, year_built,
                 soundboard_wood, strings=6):
        super().__init__(brand, model, year_built, strings)
        Wooden.__init__(self, soundboard_wood)

    def __str__(self):
        """Creates a human-readable string representation.

        Returns
        -------
        str
            Description of the acoustic guitar.
        """
        return f"{self._strings}-string " \
            + f"{self._year_built} " \
            + f"{self._brand} {self._model} " \
            + f"with {self._wood_name} soundboard"


class Clarinet(MusicalInstrument):
    """Abstract base class derived from MusicalInstrument.

    See Also
    --------
    MusicalInstrument
    """
    pass


