from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Chapter04/mersenne/num_perfecto.pyx")
)
