#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe un número entero N, y retorna un string de
# su valor absoluto, con el mensaje “El valor absoluto de N es |N|”.

def valorAbsoluto(N):
    a=abs(N)
    return 'El valor absoluto de '+str(N)+' es '+ str(a)

# Cree una función que reciba su nombre de pila, y luego retorne un string
# con la cantidad de letras de ese nombre, con el mensaje “El nombre [NOMBRE]
# tiene [N] letras.”.

def contarLetrasNombre(nombre):
    longitud=len(nombre)
    return 'El nombre '+str(nombre)+' tiene '+str(longitud)+' letras.'

# Cree una función que recibe dos números, una base y un exponente, y
# retorna el resultado de elevar el número base a la potencia exponente

def potenciacion(n1,n2):
    resultado=n1**n2
    return resultado

# Implemente una función para calcular el perímetro de un
# rectángulo, conociendo su base y altura:
# perímetro = 2 * (base + altura)

def perimetro(b,a):
    return 2*(b+a)

# Escriba una función que reciba las notas de los dos parciales de un
# alumno de la asignatura Introducción a la Programación, y retorne su promedio.

def promedioNotas(n1,n2):
    return (n1+n2)/2

# Escriba una función que reciba un monto numérico en pesos argentinos y
# retorne un string con la conversión en dólares, conteniendo la leyenda:
# "Si me das N pesos, te doy M dolares"
# Asuma un tipo de cambio U$1 = $90

def cambioDolar(p):
    d=p//90
    return 'Si me das '+str(p)+' pesos, te doy '+str(d)+' dolares'