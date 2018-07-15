def Operaciones_Binarias(numeros,numeros2,opcion):
    suma=0
    suma2=0
    cont=0
    n=1
    conversion=""
    pase="true"
    if len(numeros)>=len(numeros2):
        t=len(numeros)
    if len(numeros)<len(numeros2):
        t=len(numeros2)       
    j=len(numeros)
    while pase=="true":
        while len(numeros)<t or len(numeros2)<t:

            if len(numeros)<t:
                numeros="0"+numeros
                print numeros
                
            if len(numeros2)<t:
                numeros2="0"+numeros2
                
        while cont!=t:
            j-=1
            if numeros[j]=="1" :    
                suma=suma+n

            if numeros2[j]=="1":
                suma2=suma2+n
                
            cont+=1
            n=n*2
            
            if cont==t and opcion==1:
                pase="false"
                resultado=suma+suma2
                
            if cont==t and opcion==2:
                pase="false"
                resultado=suma-suma2
                
            if cont==t and opcion==3:
                pase="false"
                resultado=suma*suma2
                
            if cont==t and opcion==4:
                pase="false"
                resultado=suma//suma2
            
    while resultado // 2 != 0:
        conversion = str(resultado % 2) + conversion
        resultado = resultado // 2
            
    return str(resultado) + conversion

numeros=  str(input("Ingrese un numero "))
numeros2= str(input("Ingrese un numero2 "))
opcion=int(input("resta  suma "))
print "El Resultado en Decimal es: ", Operaciones_Binarias(numeros,numeros2,opcion)

