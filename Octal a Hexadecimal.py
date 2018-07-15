numero=raw_input("Ingrese un numero octal:" )
binadict = {"0" : "000","1" : "001","2" : "010","3" : "011","4" : "100","5" : "101","6" : "110","7" : "111"}
binadicth = {"0000" : "0","0001" : "1","0010" : "2","0011" : "3","0100" : "4","0101" : "5","0110" : "6","0111" : "7", "1000" : "8","1001" : "9","1010" : "a","1011" : "b","1100" : "c","1101" : "d","1110" : "e","1111" : "f"}
valor=""
hexa=""
resu=""
for i in range(len(numero)):
        k=numero[i]
        valor+=binadict.get(k)
a=len(valor)
z=len(valor)
pase=1
j=[1,2,3]

while pase==1:
       
        if a==1or a==2 or a==3 or a==4 or z==0:
                z=0
                resu=str(valor[z:a])
                while len(resu)<=len(j):
                        resu="0"+resu

                hexa=binadicth.get(resu)+hexa
                pase=0
                

        else:
                z=z-4
                resu=str(valor[z:a])
                a=a-4
                hexa=binadicth.get(resu)+hexa
                
       
                
print "el resultado es ",hexa
