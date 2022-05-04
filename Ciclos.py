#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe dos números enteros positivos n1 y n2 como 
# parámetros, donde n1 < n2, y retorna el resultado de sumar los números enteros 
# contenidos en el intervalo [n1...n2]
def sumatoria(n1, n2):
    total=0
    for nro in range(n1,n2+1):
        total+=nro
    return total

# Cree una función que recibe un número entero n mayor o igual a cero como 
# parámetro, y retorna el factorial de dicho número. Recuerde que el factorial 
# de 0 es 0!=1, el factorial de 1 es 1!=1, y el factorial de n = n! = 
# 1 * 2 * 3 * … * (n - 1) * n
def factorial(n):
    factor=1
    if(n==0 or n==1):
        salida=1
    else:
        for i in range(1,n+1):
            factor*=i
            salida=factor
    return salida

# Cree una función que recibe como parámetros dos números enteros positivos n1 y 
# n2, donde n1 < n2, y un booleano. Si el booleano fuese True, la función retorna 
# el resultado de sumar los números enteros pares contenidos en el intervalo 
# [n1...n2]. Si el booleano fuese False, la función retorna el resultado de sumar 
# los números enteros impares contenidos en el intervalo [n1...n2].
def sumaParesOImpares(n1, n2, pares):
    total=0
    if(pares==True):
        for nro in range(n1,n2+1):
            if((nro%2)==0):
                total+=nro
    else:
        for nro in range(n1,n2+1):
            if((nro%2)!=0):
                total+=nro
    return total

# Cree una función que recibe como parámetro un número entero n, donde 0 <= n < 100, 
# y retorna la sumatoria de los números enteros contenidos en el intervalo [1...100], 
# espaciados por n números.
def sumaEspaciadaDel1al100(n):
    total=0
    for i in range(1,101,n+1):
        total+=i
    return total

# Cree una función que recibe como parámetros un string y un número entero 
# positivo n, y retorna el string pasado como parámetro concatenado n veces.
def teLoRepitoNVeces(mensaje, n):
    return mensaje*n