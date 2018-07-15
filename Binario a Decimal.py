

def Binario_Decimal(numeros):
    suma=0
    cont=0
    n=1
    t=len(numeros)
    j=t
    while cont!=t:
        j-=1
        if numeros[j]=="1":
            suma=suma+n
        cont+=1
        n=n*2
    return suma

numeros=raw_input("Ingrese un numero ")
print "El Resultado en Decimal es: ", Binario_Decimal(numeros)
