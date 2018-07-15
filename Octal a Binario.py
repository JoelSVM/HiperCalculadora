def octal_binario(numero):
    valor=""
    k=0
    bina = ["000","001","010","011","100",
            "101","110","111"]

    for i in range(len(numero)):
        k=int(numero[i])
        valor+=bina[k]
    return valor

numero=raw_input("Ingrese un numero octal:" )
print "el resultado es ",(octal_binario(numero))




