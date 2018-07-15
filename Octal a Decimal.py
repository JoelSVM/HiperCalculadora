
# -*- coding: cp1252 -*-
def octal_decimal(bits):
  aList=[]
  n=len(bits)
  valor=0
  k=0
  c=0
  for i in range(len(bits)):
    aList.append(8**(n-1))
    n -=1
    k=int(aList[i])
    c=int(bits[i])
    valor+=k*c
    
  return valor

    
bits=raw_input('Dame un número octal: ')  
print 'Su valor decimal es',(octal_decimal(bits))




