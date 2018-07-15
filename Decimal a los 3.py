
# -*- coding: cp1252 -*-
def cambio_base(decimal,base):
    binadicth = {"10" : "a","11" : "b","12" : "c","13" : "d","14" : "e","15" : "f"}
    aList=[]
    conversion = ""
    if base==16:
        while decimal // base != 0:
            aList.append(str(decimal % base))
            decimal = decimal // base
            
        for i in range(len(aList)):
            if aList[i] in binadicth:
                conversion=str(binadicth.get(aList[i]))+conversion
            else:
                conversion=aList[i]+conversion
                    
    else:
        while decimal // base != 0:
            conversion = str(decimal % base) + conversion
            decimal = decimal // base
    return str(decimal) + conversion

numero = int(input(" Ingrese los valores: "))
base = int(input("ingrese la base: "))
print(cambio_base(numero, base))

 
                
                
	

