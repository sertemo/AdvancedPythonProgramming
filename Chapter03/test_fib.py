"""Después de compilar el fib.pyx, ejecuta este código para probarlo:"""

from fib import fib
from slow_fib import fib_py

import time


s = time.perf_counter()
print(fib(40))
print("Versión Cython", time.perf_counter() - s)


s = time.perf_counter()
print(fib_py(40))
print("Versión Python", time.perf_counter() - s)