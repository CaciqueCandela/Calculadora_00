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

# Calcular suma:

    suma = lambda numero1, numero2: numero1 + numero2

# Calcular resta:

    resta = lambda numero1, numero2: numero1 - numero2

# Calcular el multiplicación:

    multiplicacion = lambda numero1, numero2: numero1 * numero2

# Calcular división:

    division = lambda numero1, numero2: numero1 / numero2

# Ingresamos los valores:

    print("\nCALCULADORA DE OPERACIONES BÁSICAS UTILIZANDO DOS VALORES MEDIANTE LAMBDAS")

    numero1 = float(input("\nPor favor ingrese el primer valor a utilizar y presione Enter: "))
    numero2 = float(input("Por favor ingrese el segundo valor a utilizar y presione Enter: "))
   
    # Ahora se deben ingresar las operaciones:

    def Calculadora():
        fin = False
        while not(fin):
            operation = input("\nIndique el número de la operación que desea realizar y presione Enter: ")
    
            if operation == "1":
                print('\nLa suma da como resultado: ', numero1 + numero2)

            elif operation == "2":
                print('\nLa diferencia da como resultado: ', numero1 - numero2)

            elif operation == "3":
                print('\nEl producto da como resultado: ', numero1 * numero2)

            elif operation == "4":
                print('\nEl cociente da como resultado: ',int(numero1 / numero2))

            elif operation == "5":
                fin = 1

            else:
                print("\nNúmero incorrecto.")

    print("""
    \t1) Suma
    \t2) Resta
    \t3) Multiplicación
    \t4) División
    \t5) Salir
    
    """)
    Calculadora()
    

if __name__ == '__main__':
    run()
