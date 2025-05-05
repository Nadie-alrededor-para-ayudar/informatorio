# Definir la lista de números del 1 al 1000
numeros = list(range(1, 1001))

# Lista donde vamos a guardar los números primos
numeros_primos = []

# Recorremos cada número de la lista
for numero in numeros:
    if numero > 1:  # Los primos son mayores que 1
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numero)

# Mostramos la lista de números primos
print(numeros_primos)