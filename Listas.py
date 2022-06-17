#################################################
# Funciones que tenés que programar
#################################################


# Cree una función que recibe una lista l de números enteros y retorna una lista
# de los números pares de la lista l, conservando el orden que tenían dichos
# números pares en la lista l. Si no hay ningún número par en la lista l, deberá
# retornar una lista vacía.
# Ejemplo, si l=[1,0,-4,-5,2,0] deberá retornar la lista [0,-4,2,0]
def extraePares(l):
    r=[]
    for i in range(len(l)):
        if (l[i]%2) == 0:
            r.append(l[i])
    return r

# Cree una función que recibe una lista no vacía l de números enteros y retorna 
# un entero m con la multiplicación de todos los números de la lista, y un número 
# entero s con la sumatoria de los elementos de la lista l.
# Ejemplo: l=[-1,2,3] debe retornar (-6,4)
# Ejemplo: l=[-1,0,3] debe retornar (0,2)
def productoriaYSumatoria(l):
    s=0
    m=1
    for i in range(len(l)):
        m*=l[i]
        s+=l[i]
    return m,s

# Cree una función que recibe como parámetros una lista l no vacía de números 
# enteros, dos números enteros naturales n1 y n2, donde 0<=n1<=n2<len(l), y 
# un booleano. Si el booleano fuese True, la función retorna 
# el resultado de sumar los números enteros pares contenidos en el intervalo 
# l[n1...n2] (si no hay ningún número par en el intervalo retorna 0). Si el 
# booleano fuese False, la función retorna el resultado de sumar los números 
# enteros impares contenidos en el intervalo l[n1...n2] (si no hay ningún número 
# impar en el intervalo retorna 0).
def sumaSubcadena(l, n1, n2, pares):
    suma=0
    if (pares==True):
        for i in range(n1,n2+1):
            if(l[i]%2==0):
                suma+=l[i]
    elif(pares==False):
        for i in range(n1,n2+1):
            if(l[i]%2==1):
                suma+=l[i]
    return suma