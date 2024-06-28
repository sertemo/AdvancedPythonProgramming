def es_primo(n: int) -> bool:
    """Devuelve si un número es primo o no"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        
        i += w
        w = 6 - w

    return True

def generar_num_perfecto(p: int) -> int:
    """Devuelve un numero perfecto dada una potencia si se cumple
    2^p - 1 es primo"""
    mersenne = (2 ** p - 1)
    if es_primo(mersenne):
        return 2 ** (p - 1) * mersenne

def obtener_divisores(n: int) -> list:
    """Devuelve una lista de los divisores"""

    divisores = []
    divisores_ext = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // 1:
                divisores_ext.insert(0, n // i)
    return divisores + divisores_ext[:-1]

def print_mersenne(p: int, show_divisores: bool = False) -> None:
    for num in range(p):
        if (perfecto := generar_num_perfecto(num)) is not None:
            divi = f"| Divisores: {obtener_divisores(perfecto)}" if show_divisores else ""
            print(perfecto, divi)

if __name__ == '__main__':
    print_mersenne(10, show_divisores=False)