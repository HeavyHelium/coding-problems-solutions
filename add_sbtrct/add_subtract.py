from __future__ import annotations
from collections.abc import Callable

class Alternator: 
    operations: list[Callable] = [ lambda x, y: x + y, 
                                   lambda x, y: x - y ]

    def __init__(self, init_value: int = 0) -> None:
        self._value = init_value
        self._operation = 0

    def _next_operation(self) -> None:
        self._operation = (self._operation + 1) % len(self.operations)

    def __call__(self, rhs: int) -> Alternator:
        self._value = self.operations[self._operation](self._value, rhs)
        self._next_operation()
        return self
    
    def __repr__(self) -> str:
        return f"Alternator({self._value})"
    
    def __str__(self) -> str:
        return str(self._value)
    
def add_subtract(init_value: int = 0) -> Alternator:
    return Alternator(init_value)
    

if __name__ == "__main__":
    print(add_subtract(1)(2)(3))
    print(add_subtract(1)(2)(3)(4)(5))
    print(add_subtract(-5)(10)(3)(9))
    