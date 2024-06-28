import time
import sys, os

# Añadir la ruta del directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Chapter04.mersenne import num_perfecto
from Chapter04.mersenne import mersenne_py

n = 32

if __name__ == '__main__':

    # Cython
    print("n=", n)

    print("Cython")
    s = time.perf_counter()
    num_perfecto.print_mersenne(n, show_divisores=False)
    print("Tiempo empleado:", time.perf_counter() - s)
    print("##########################")

    print("Python")
    s = time.perf_counter()
    mersenne_py.print_mersenne(n, show_divisores=False)
    print("Tiempo empleado:", time.perf_counter() - s)

