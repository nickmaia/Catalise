from scipy import integrate
from math import exp
from scipy.integrate import quad
import numpy as np


def calculate_temp_pfr_ordem_um_doisreagentes(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao, cbo
):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    teta_b = cbo / cao

    def malha(func, a, b, n):
        x = np.linspace(a, b, n + 1, dtype=float)
        y = func(x)
        h = (b - a) / n
        return y, h

    def integral_simpson(func, a, b, n):
        if int(n) % 2:  # para garantir numero par de intervalos
            n += 1
        y, h = malha(func, a, b, n)
        Si = np.sum(y[1:-1:2])  # posicoes impares
        Sp = np.sum(y[2:-1:2])  # posicoes pares
        S = y[0] + 4.0 * Si + 2.0 * Sp + y[-1]
        return h * S / 3.0

    def f(x):
        return qo / (k2 * cao * (1 - x) * (teta_b - x))

    print(integral_simpson(f, 0, x, 100))


"""def calculate_temp_pfr_ordem_um_doisreagentes(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao, cbo
):
    
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr)/((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    teta_b = cbo / cao

    def reaction_rate(x):
        return (qo / (k2 * cao * (1 - x) * (teta_b - x)))

    volume, _ = quad(reaction_rate, 0, x)
    print(volume)
    return round(volume, 4)"""

calculate_temp_pfr_ordem_um_doisreagentes(
    300, 35.9999999999712, 125.604, 300, 273, -25104, 0, 0.85, 7200, 10000, 0.1, 0.1
)

"""# Importa o método
from scipy import integrate

# Declara a funcao
funcao = lambda x: x**2

#Calcular integral simples dusando o método QUADPACK da biblioteca FORTRAN
resultado = integrate.quad(funcao, 0.0, 5.0)

print("Resultado da integração:" )
print(resultado[0])
print("Erro calculado da integração:" )
print(resultado[1])"""

"""
def malha(func, a, b, n):
    x = np.linspace(a, b, n+1, dtype=float)
    y = func(x)
    h = (b - a) / n
    return y, h
def integral_simpson(func, a, b, n):
    if int(n) % 2: # para garantir numero par de intervalos
        n += 1
    y, h = malha(func, a, b, n)
    Si = np.sum(y[1:-1:2]) # posicoes impares
    Sp = np.sum(y[2:-1:2]) # posicoes pares
    S = y[0] + 4. * Si + 2. * Sp + y[-1]
    return h * S / 3.

def f(x):
    return np.sin(x)
print(integral_simpson(f, 0, np.pi, 100))"""
