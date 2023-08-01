def d2x(n, x):
    if n == 0:
        return "0"
    resultado = ""
    while n > 0:
        resto = n % x
        resultado = str(resto) + resultado
        n //= x
    return resultado