# cython: boundscheck=False, wraparound=False
cimport cython
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bint es_primo(double n):
    """Devuelve si un número es primo o no"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    cdef int i = 5
    cdef int w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        
        i += w
        w = 6 - w

    return True

cpdef double generar_num_perfecto(double p):
    """Devuelve un numero perfecto dada una potencia si se cumple
    2^p - 1 es primo"""
    cdef double mersenne = (2 ** p) - 1
    if es_primo(mersenne):
        return (2 ** (p - 1)) * mersenne
    return -1

cpdef list obtener_divisores(double n):
    """Devuelve una lista de los divisores"""
    cdef double i
    cdef list divisores = []
    cdef list divisores_ext = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores_ext.insert(0, n // i)
    return divisores + divisores_ext

cpdef void print_mersenne(int p, bint show_divisores):
    cdef int num
    cdef double perfecto
    cdef list divi

    for num in range(p):
        perfecto = generar_num_perfecto(num)
        if perfecto != -1:
            if show_divisores:
                divi = obtener_divisores(perfecto)
                print(perfecto, "| Divisores:", divi)
            else:
                print(perfecto)



