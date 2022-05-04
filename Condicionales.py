#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe un número entero N como parámetro, y retorna un 
# booleano. Si el número N es mayor que cero, retorna True. Si el número N es 
# menor o igual a cero, retorna False
def numeroPositivo(x):
    if (x>0):
        respuesta=True
    else:
        respuesta=False
    return respuesta

# Cree una función que recibe un string como parámetro, y retorna un string con 
# la leyenda "Sos Maria", si el string recibido de argumento fuese "Maria", 
# "Sos Pedro" si el string recibido fuese "Pedro", "No sos Maria ni Pedro. Quien sos?" 
# si el string recibido como argumento no fuese "Maria" ni "Pedro"
def quienSos(x):
    if(x=="Maria"):
        return "Sos Maria"
    elif(x=="Pedro"):
        return "Sos Pedro"
    else:
        return "No sos Maria ni Pedro. Quien sos?"
    
# Cree una función que recibe dos números de parámetro, y retorna el menor de 
# ellos, si los números fuesen distintos. Si los números fuesen iguales, debe 
# retornar el string "Son iguales!"
def dameElMenorODecimeSiSonIguales(x, y):
    if(x==y):
        return "Son iguales!"
    elif(x<y):
        return x
    else:
        return y

# Cree una función que recibe un número entero entre 1 y 12 de parámetro, 
# correspondiente a un mes y retorna un  string, con el nombre del mes en 
# lenguaje natural. La relación entre números y meses es la siguiente: 1 Enero, 
# 2 Febrero, 3 Marzo, 4 Abril, 5 Mayo, 6 Junio, 7 Julio, 8 Agosto, 9 Septiembre, 
# 10 Octubre, 11 Noviembre, 12 Diciembre
def decimeElMes(x):
    if(x==1):
        return "Enero"
    elif(x==2):
        return "Febrero"
    elif(x==3):
        return "Marzo"
    elif(x==4):
        return "Abril"
    elif(x==5):
        return "Mayo"
    elif(x==6):
        return "Junio"
    elif(x==7):
        return "Julio"
    elif(x==8):
        return "Agosto"
    elif(x==9):
        return "Septiembre"
    elif(x==10):
        return "Octubre"
    elif(x==11):
        return "Noviembre"
    else:
        return "Diciembre"

# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes y retorna un  string, con el nombre de la estación. Considera la 
# relación entre números y estaciones de la siguiente forma: 1, 2, 3: "Verano", 
# 4, 5, 6: "Otoño", 7, 8, 9: "Invierno", 10, 11, 12: "Primavera"
def estacion(x):
    if(x>=1) and (x<=3):
        return "Verano"
    elif(x>=4) and (x<=6):
        return "Otoño"
    elif(x>=7) and (x<=9):
        return "Invierno"
    else:
        return "Primavera"

# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes, y retorna un booleano, que es True si el número del mes fuese par, 
# y False si el número del mes fuese impar
def mesPar(x):
    if((x%2)==0):
        return True
    else:
        return False

# Cree una función que recibe dos números entre 0 y 10, correspondientes a las
# notas de los exámenes, y retorna un string con la leyenda "Promovido", si el 
# promedio de dichos númueros, fuese mayor o igual a 8, "Regular", si el promedio
# fuese mayor o igual a 4 pero menor a 8, y "Libre" si el promedio de las notas
# fuese menor a 4
def situacionAlumno(p1, p2):
    promedio=(p1+p2)/2
    if(promedio>=8):
        return "Promovido"
    elif(promedio>=4) and (promedio<8):
        return "Regular"
    else:
        return "Libre"

# En un triángulo la longitud de cada lado es menor que la suma de los otros dos.
# Cree una función que recibe 3 enteros como parámetros, y retorna un booleano 
# que es True en el caso de que los valores recibidos puedan corresponder a las 
# longitudes de los lados de un triángulo y False en caso contrario. Recuerde 
# que ninguna de las longitudes de los lados de un triángulo puede ser cero, 
# o números negativos.
def esTriangulo(x, y, z):
    if(x<=0) or (y<=0) or (z<=0):
        return False
    elif(x<y+z) and (y<x+z) and (z<x+y):
        return True
    else:
        return False

# Cree una función que recibe 3 números enteros como parámetros, y retorna un 
# string con la leyenda:
# "No es un triangulo", si los longitudes no pueden corresponder a un triángulo
# "Equilatero", si puede ser un triángulo y todos las longitudes son iguales
# "Isosceles", si puede ser un triángulo y tiene dos longitudes iguales
# "Escaleno", si puede ser un triángulo y todas las longitudes son diferentes
def tipoTriangulo(x, y, z):
    if(x<=0) or (y<=0) or (z<=0):
        return "No es un triangulo"
    elif(x<y+z) and (y<x+z) and (z<x+y):
        if(x==y) and (y==z):
            return "Equilatero"
        elif(x==y) or (y==z) or (x==z):
            return "Isosceles"
        else:
            return "Escaleno"
    else:
        return "No es un triangulo"