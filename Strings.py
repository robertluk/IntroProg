#################################################
# Funciones que tenés que programar
#################################################


# Cree una función que recibe un string s de longitud > 0, y dos números enteros 
# naturales n y m, donde 0<=n<=m<len(s), y retorna un nuevo string t que 
# es el string s sin la subcadena s[n1..n2].
# Ejemplo: s="Hola", n=1, m=2, retorna "Ha"
# Ejemplo: s="Hola", n=1, m=1, retorna "Hla" 
# Ejemplo: s="Hola", n=3, m=3, retorna "Hol"
# Ejemplo: s="Hola", n=0, m=3, retorna ""
# string, que es el resultado 
def borrarSubcadena(s,n,m):
    S=""
    longitud=len(s)
    for i in range(longitud):
        if not(i in range(n,m+1)):
            S+=s[i] 
    return(S)

# Cree una función que recibe un string s, y retorna dos enteros n y m, siendo
# n la cantidad de vocales minúsculas, y m la cantidad de vocales mayúsculas,
# que tiene el string s.
def contadorVocales(s):
    vocales_M=0
    vocales_m=0
    for i in range(len(s)):
        if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
            vocales_M+=1
        elif s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
            vocales_m+=1
    return vocales_m,vocales_M