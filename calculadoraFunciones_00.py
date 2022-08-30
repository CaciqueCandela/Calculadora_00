# CALCULADORA UTILIZANDO FUNCIONES

'''
Ejercicio: realizar una calculadora que permita las siguientes funciones:
> Sumar dos números.
> Restar dos números.
> Multiplicar dos números.
> Dividir dos números.
> Calcular el factorial de un número.
> Calcular la potencia de un número.
'''

# Primero se deben definir las operaciones mediante funciones.

def run():

    # Calcular suma:

    def suma(numero1, numero2):
        return numero1 + numero2

    # Calcular resta:

    def resta(numero1, numero2):
        return numero1 - numero2

    # Calcular el multiplicación:

    def multiplicacion(numero1, numero2):
        return numero1 * numero2

    # Calcular división:

    def division(numero1, numero2):

        try:
            return numero1 / numero2

        except ZeroDivisionError:
            print('No se puede dividir entre 0')
            return "Operación errónea."

    # Calcular el factorial:

    '''def factorial(numero1):
        if numero1 < 0:
            return None

        if numero1 < 2:
            return 1

        return numero1 * factorial(numero1 - 1) # Esta es nuestra función recursiva.'''

    # Calcular la potencia:

    def Potencia(numero1, numero2):
        if numero2 <= 0:
            return 1

        else:
            return numero1 * Potencia(numero1, numero2-1)

    # Ingresamos los valores:

    print("\nCALCULADORA DE OPERACIONES BÁSICAS UTILIZANDO DOS VALORES\n")
    
    print("""
    \t*Si la operación que desea realizar es una suma ingrese el simbolo +
    \t*Si la operación que desea realizar es una resta ingrese el simbolo -
    \t*Si la operación que desea realizar es una multiplicación ingrese el simbolo *
    \t*Si la operación que desea realizar es una división ingrese el simbolo /
    \t*Si la operación que desea realizar es una potencia ingrese el simbolo &

    """)
    operation = input("\nIndique qué operación desea realizar y presione Enter: ")

    numero1 = int(input("\nPor favor ingrese el primer valor y presione Enter: "))
    numero2 = int(input("Por favor ingrese el segundo valor y presione Enter: "))
    
    # Ahora se deben ingresar las operaciones:

    if operation == "+":
        print('\nLa suma da como resultado: ', numero1 + numero2)

    elif operation == "-":
        print('\nLa diferencia da como resultado: ', numero1 - numero2)

    elif operation == "*":
        print('\nEl producto da como resultado: ', numero1 * numero2)

    elif operation == "/":
        print('\nEl cociente da como resultado: ', numero1 / numero2)

        '''elif operation == "!":
        print('\nEl número factorial de', (numero1), 'es', factorial(numero1) )'''

    elif operation == "&":
        print('\nEl valor de ' + str(numero1) + ' elevado a ' + str(numero2) + ' es: ' + str(Potencia(numero1, numero2)))

    else:
        print("\nOperación o simbolo incorrecto.")

if __name__ == '__main__':
    run()