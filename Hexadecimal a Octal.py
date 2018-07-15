numero=raw_input("Ingrese un numero Hexadecimal: " )
binadict = {"000" : "0","001" : "1","010" : "2","011" : "3","100" : "4","101" : "5","110" : "6","111" : "7"}
binadicth = {"0" : "0000" ,"1" : "0001","2" : "0010","3" : "0011","4" : "0100","5" : "0101","6" : "0110","8" : "0111", "8" : "1000","9" : "1001","a" : "1010","b" : "1011","c" : "1100","d" : "1101","e" : "1110","f" : "1111"}
valor=""
octa=""
resu=""
for i in range(len(numero)):
        k=numero[i]
        valor+=binadicth.get(k)
a=len(valor)
z=len(valor)
pase=1
j=[1,2]

while pase==1:
       
        if a==1 or a==2 or a==3 or z==0:
                z=0
                resu=str(valor[z:a])
                while len(resu)<=len(j):
                        resu="0"+resu

                octa=binadict.get(resu)+octa
                pase=0
                

        else:
                z=z-3
                resu=str(valor[z:a])
                a=a-3
                octa=binadict.get(resu)+octa
                
       
                
print "el resultado es ",octa
