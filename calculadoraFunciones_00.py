# CALCULADORA UTILIZANDO FUNCIONES LAMBDA

'''
Ejercicio: realizar una calculadora que permita las siguientes operaciones:
> Sumar dos números.
> Restar dos números.
> Multiplicar dos números.
> Dividir dos números.
> Calcular el factorial de un número.
> Calcular la potencia de un número.
'''

# Primero se deben definir las operaciones mediante funciones Lambda.

def run():

    print("\nCALCULADORA DE OPERACIONES BÁSICAS UTILIZANDO DOS VALORES MEDIANTE LAMBDAS")

    #operation = input("\nIndique el número de la operación que desea realizar y presione Enter: ")
    
    num1 = float(input("\nPor favor ingrese el primer valor a utilizar y presione Enter: "))
    num2 = float(input("Por favor ingrese el segundo valor a utilizar y presione Enter: "))

# Calcular suma:

    suma = lambda num1, num2: num1 + num2
    print(suma(num1, num2))

# Calcular resta:

    resta = lambda numero1, numero2: numero1 - numero2

# Calcular el multiplicación:

    multiplicacion = lambda numero1, numero2: numero1 * numero2

# Calcular división:

    division = lambda numero1, numero2: numero1 / numero2

# Ingresamos los valores:


    

if __name__ == '__main__':
    run()
