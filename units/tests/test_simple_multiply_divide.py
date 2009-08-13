"""Tests of simple multiplication and division of units and quantities."""

from units import Unit
from units.quantity import Quantity
from units.named_composed_unit import NamedComposedUnit

def test_simple_multiply():
    """Simple multiplication of units."""
    assert Unit('m') * Unit('s') / Unit('s') == Unit('m')

def test_simple_divide():
    """Simple division of units."""
    assert Unit('m') / Unit('s') * Unit('s') == Unit('m')

def test_commutative_multiply():
    """Commutative multiplication of units"""
    
    assert Unit('m') * Unit('s') / Unit('m') == Unit('s')

def test_simple_multiply_quantity():
    """Simple multiplication of quantities"""
    assert (Quantity(2, Unit('m')) * 
            Quantity(2, Unit('s')) ==
            Quantity(4, Unit('m') * Unit('s')))
            
    assert (Quantity(2, Unit('s')) * 
            Quantity(2, Unit('m')) ==
            Quantity(4, Unit('m') * Unit('s')))

def test_simple_divide_quantity():
    """Simple division of quantities"""
    assert (Quantity(8, Unit('m')) / 
            Quantity(2, Unit('s')) ==
            Quantity(4, Unit('m') / Unit('s')))
            
def test_multiply_scalar():
    """Quantities * scalars"""
    assert (Quantity(8, Unit('m')) * 2 ==
            Quantity(16, Unit('m')))

def test_rmultiply_scalar():
    """Scalars * quantities"""
    assert (2 * Quantity(8, Unit('m')) ==
            Quantity(16, Unit('m')))

def test_divide_scalar():
    """Quantities / scalars"""
    assert (Quantity(8, Unit('m')) / 2 ==
            Quantity(4, Unit('m')))

def test_rdivide_scalar():
    """Scalars / quantities"""
    assert (4 / Quantity(2, Unit('m')) ==
            Quantity(2, Unit('m').invert()))

def test_multiply_composed_scalar():
    """Composed quantities * scalars"""
    m_per_s = Unit('m') / Unit('s')
    
    assert (Quantity(8, m_per_s) * 2 ==
            Quantity(16, m_per_s))

def test_rmultiply_composed_scalar():
    """Scalars * Composed quantities"""
    m_per_s = Unit('m') / Unit('s')

    assert (2 * Quantity(8, m_per_s) ==
            Quantity(16, m_per_s))

def test_divide_composed_scalar():
    """Composed quantities / scalars"""
    m_per_s = Unit('m') / Unit('s')

    assert (Quantity(8, m_per_s) / 2 ==
            Quantity(4, m_per_s))

def test_rdivide_composed_scalar():
    """Scalars / composed quantities"""
    m_per_s = Unit('m') / Unit('s')

    assert (4 / Quantity(2, m_per_s) ==
            Quantity(2, Unit('s') / Unit('m')))

def test_multiply_named_scalar():
    """Named quantities * scalars"""
    m_per_s = NamedComposedUnit('vel', 
                                Unit('m') / Unit('s'))
    
    assert (Quantity(8, m_per_s) * 2 ==
            Quantity(16, m_per_s))

def test_rmultiply_named_scalar():
    """Scalars * Named quantities"""
    m_per_s = NamedComposedUnit('vel', 
                                Unit('m') / Unit('s'))

    assert (2 * Quantity(8, m_per_s) ==
            Quantity(16, m_per_s))

def test_divide_named_scalar():
    """Named quantities / scalars"""
    m_per_s = NamedComposedUnit('vel', 
                                Unit('m') / Unit('s'))

    assert (Quantity(8, m_per_s) / 2 ==
            Quantity(4, m_per_s))

def test_rdivide_named_scalar():
    """Scalars / Named quantities"""
    m_per_s = NamedComposedUnit('vel', 
                                Unit('m') / Unit('s'))

    assert (4 / Quantity(2, m_per_s) ==
            Quantity(2, Unit('s') / Unit('m')))


Unit.Registry.clear()
assert len(Unit.Registry) == 0