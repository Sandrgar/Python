print ("Corso Python")

def paridispari ():
    inp = input("inserisci un numero:")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print ("Il numero è Pari")
    else: 
        print ("Il numero è Dispari")

paridispari()