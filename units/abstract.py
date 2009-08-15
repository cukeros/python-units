"""An abstract base class to define the interface for all units."""

from units.compatibility import compatible
from units.exception import IncompatibleUnitsException
from units.quantity import Quantity

class AbstractUnit(object):
    """Parent class/interface for units."""
    
    def __init__(self, is_si):
        self._si = is_si
        
    def __call__(self, quantity):
        """Overload the function call operator to convert units."""
        if compatible(self, quantity.unit):
            return Quantity(quantity.num * quantity.unit.squeeze(), self)
        else:
            raise IncompatibleUnitsException()

    def canonical(self):
        """Return an immutable, comparable derivative of this unit"""
        raise NotImplementedError
            
    def invert(self):
        """Return (this unit)^-1."""
        raise NotImplementedError
                    
    def is_si(self):
        """Whether it makes sense to give this unit an SI prefix."""
        return self._si
        
    def squeeze(self):
        """Return this unit's implicit quantity multiplier."""
        raise NotImplementedError
        
        