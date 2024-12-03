from numbers import Real
from typing import Any

class AdvancedNumber:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __repr__(self) -> str:
        return f"AdvancedNumber({self.value})"
    
    def __str__(self) -> str:
        return f"Value: {self.value}"
    
    def __add__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        
        if isinstance(other, Real):
            return AdvancedNumber(self.value * other)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        return NotImplemented
    
    def __hash__(self):
        return hash(self.value)
    
    def __bool__(self):
        if self.value !=0:
            return True
        else:
            return False
        
    def __call__(self):
        return self.value * self.value
    
    def __format__(self, format_spec):
        if format_spec.endswith('f'):
            return format(self.value, format_spec)
        elif format_spec == '#x' and isinstance(self.value, int):
            return format(self.value, format_spec)
        else:
            return str(self.value)
        
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")
    
