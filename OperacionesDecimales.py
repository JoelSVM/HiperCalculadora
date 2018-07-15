def Operaciones_Decimales(numero,numero2,op):
    resultado=0
    if(op==1):
        resultado=numero+numero2
        
    if(op==2):
        resultado=numero-numero2
        
    if(op==3):
        resultado=numero*numero2
        
    if(op==4):
        resultado=numero//numero2

    return resultado

numero=int(input("Ingrese un numero decimal: "))
op=int(input("Ingrese la operacion: "))
numero2=int(input("Ingrese un numero decimal: "))

print"El Resultado es: ", Operaciones_Decimales(numero,numero2,op)       
