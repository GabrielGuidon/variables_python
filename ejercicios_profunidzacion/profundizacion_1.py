# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print('Ingrese Primer Numero')
primer_numero = int( input())
print('Ingrese Segundo Numero')
segundo_numero = int( input())
suma=primer_numero+segundo_numero
resta=primer_numero-segundo_numero
multiplicacion=primer_numero*segundo_numero
division=primer_numero/segundo_numero
potencia=primer_numero**segundo_numero
print('El resultado del primer numero mas el segundo numero es: ', suma)
print('El resultado del primer numero menos el segundo numero es: ', resta)
print('El resultado del primer numero multiplicado el segundo numero es: ', multiplicacion)
print('El resultado del primer numero dividido el segundo numero es: ', division)
print('El resultado del primer numero elevado al segundo numero es: ', potencia)

