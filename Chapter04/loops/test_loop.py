"""Después de compilar el loop.pyx, ejecuta este código para probarlo:"""

from loop import loop_cython
from slow_loop import loop_py

import time

n = 100_000_000

print("Para un loop de n=", n)
s = time.perf_counter()
loop_cython(n)
print("Versión Cython:", time.perf_counter() - s, "s")


s = time.perf_counter()
loop_py(n)
print("Versión Python:", time.perf_counter() - s, "s")