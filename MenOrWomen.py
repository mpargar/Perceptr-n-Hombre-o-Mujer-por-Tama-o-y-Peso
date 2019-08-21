umbral = 0.5
tasa_de_aprendizaje = 0.1
pesos = [0, 0]
conjunto_de_entrenamiento = [
    ((170,56),1), # Mujer de 1.70m y 56kg
    ((172,63),0), # Hombre de 1.72m y 63kg
    ((160,50),1), # Mujer de 1.60m y 50kg
    ((170,63),0), # Hombre de 1.70m y 63kg
    ((174,66),0), # Hombre de 1.74m y 66kg
    ((158,55),1), # Mujer de 1.58m y 55kg
    ((183,80),0), # Hombre de 1.83m y 80kg
    ((182,70),0), # Hombre de 1.82m y 70kg
    ((165,54),1) # Mujer de 1.65m y 54kg
]

def producto_punto(valores, pesos):
    return sum(valor * peso for valor, peso in zip(valores, pesos))

# Entrenamiento
print('-' * 73)
print(('-' * 30) + 'Entrenamiento' + ('-' * 30))
while True:
    print('-' * 73)
    contador_de_errores = 0
    for vector_de_entrada, salida_deseada in conjunto_de_entrenamiento:
        print(pesos)
        resultado = producto_punto(vector_de_entrada, pesos) > umbral
        error = salida_deseada - resultado
        if error != 0:
            contador_de_errores += 1
            for indice, valor in enumerate(vector_de_entrada):
                pesos[indice] += tasa_de_aprendizaje * error * valor
    if contador_de_errores == 0:
        break

print('\n' * 5)
print('-' * 73)
print(('-' * 33) + 'Calculo' + ('-' * 33))
print('-' * 73)

altura = float(input("Introduce tu estatura en centimetros.- "))
peso = float(input("Introduce tu peso en kilogramos.- "))
p_p = producto_punto((altura, peso), pesos)
print('Producto punto: ' + str(p_p))
print('Umbral: ' + str(umbral))
print('Resultado: ' + ('Mujer' if p_p > umbral else 'Hombre'))