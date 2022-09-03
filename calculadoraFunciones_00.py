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


print('Prototipo de calculadora con operaciones básicas')
print()

# Primero se deben definir las operaciones mediante funciones.

def run():

# Función para suma:

    from re import X


    def suma():
        numero1 = int(input('Por favor, ingrese el sumando uno: '))
        numero2 = int(input('Por favor, ingrese el sumando dos: '))
        print('La suma de ', numero1, '+', numero2, 'es', numero1+numero2)

# Función para resta:

    def resta():
        numero1 = int(input('Por favor, ingrese el minuendo: '))
        numero2 = int(input('Por favor, ingrese el sustraendo: '))
        print('La diferencia de ', numero1, '-', numero2, 'es', numero1-numero2)

# Función para multiplicación:

    def multiplicacion():
        numero1 = int(input('Por favor, ingrese el multiplicando: '))
        numero2 = int(input('Por favor, ingrese el multiplicador: '))
        print('El producto de ', numero1, '*', numero2, '=', numero1*numero2)

# Función para división:

    def division():
        try:
            numero1 = int(input('Por favor, ingrese el dividendo: '))
            numero2 = int(input('Por favor, ingrese el divisor: '))
            print('El cociente de ', numero1, '/', numero2, '=', numero1/numero2)
        except ZeroDivisionError:
            print('ERROR: no se puede dividir por cero')

    
# Calcular el factorial: 
    '''Cantidad que resulta de la multiplicación de determinado número natural por
    todos los números naturales que le anteceden excluyendo el cero; se representa por n!)'''

    def factorial():
        mi_factorial = int(input('\nPor favor, introduzca el número del que quiere calcular el factorial: '))
        print('El factorial de', str(mi_factorial), 'es:', str(factorialCalculo(mi_factorial)))

    def factorialCalculo(numero):
        if numero <= 1: # No puede ser 0 porque cualquier multiplicación por 0 = 0.
            return 1
        else:
            # Es el resultado de multiplicar un número por todos los números anteriores.
            return numero * factorialCalculo(numero - 1) 

# Calcular la potencia:
# Resultado de multiplicar un número por sí mismo una o varias veces.

    def potencia():
        base = int(input('Por favor, ingrese la base de la potencia: '))
        exponente = int(input('Por favor, ingrese el exponente de la potencia: '))
        print('\nEl valor de ' + str(base) + ' elevado a ' + str(exponente) + ' es: ' + str(potenciaCalculo(base, exponente)))

    def potenciaCalculo(base, exponente):
        if exponente <= 0:
            return 1

        else:
            return base * potenciaCalculo(base, exponente-1)

# Calcular la raíz cuadrada (Método babilónico):
    '''
    La raíz cuadrada es una operación matemática que se realiza sobre un número para conocer qué otro número,
    multiplicado por sí mismo, da como resultado el número original.
    '''

    def raiz_cuadrada():
        numero1 = int(input('Por favor, ingrese el radicando: '))
        print('La raíz cuadrada de ', numero1, 'es', raiz_babilonica(numero1))
    
    def raiz_babilonica(numero1):
        x = numero1 / 2

        while True: # Necesitamos un bucle
            if x * x == numero1:
                return x # x
            else:
                copia_x = x
                # Calculamos la media entre la base y la altura. "numero1" sería el área. "x" sería la base.
                x = (x + (numero1/x)) / 2 
            if copia_x == x:
                break
            # "x" que es la base del rectangulo se iría acercando a la base del rectangulo que buscamos.
        return x


# Segundo, se ingresa la función para la calculadora:

    def Calculadora():
        fin = False
        while not(fin):
            opcion = int(input('Por favor, escoge una opción y presiona Enter: '))
            if (opcion == 1):
                suma()
            elif (opcion == 2):
                resta()
            elif (opcion == 3):
                multiplicacion()
            elif (opcion == 4):
                division()
            elif (opcion == 5):
                factorial()
            elif (opcion == 6):
                potencia()
            elif (opcion == 7):
                raiz_cuadrada()  
            elif (opcion == 8):
                fin = 1
            else:
                print('\nOpción incorrecta.')
                    
    # Ingresamos los valores:

    print('''\nCALCULADORA DE OPERACIONES BÁSICAS UTILIZANDO DOS VALORES BASADA EN FUNCIONES DE PYTHON
        \nMenu:
        1) Suma
        2) Resta
        3) Multiplicación
        4) División
        5) Factorial
        6) Potencia
        7) Raíz cuadrada
        8) Salir\n''')
    Calculadora()


if __name__ == '__main__':
    run()
