# Programa para calcular el número de meses que seduplica el capital

# -----------------
# libraries
# -----------------

print("-------------------------------------------------------------------------")
print("------------Calculo del numero de meses que se duplica el capital--------")
print("-------------------------------------------------------------------------")
import math

# -----------------
# Intput
# -----------------

c= int(input("Digita tu capital:$ "))

# -----------------
# Procesing
# -----------------
d = 2*c
n = 0
while c < d:
    c = c * 1.05
    n = n + 1

# -----------------
#outpt UwU
# -----------------

print("Su capital se ha duplicado en", n, "meses.")
