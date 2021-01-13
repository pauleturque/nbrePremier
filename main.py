# programme fonction nombre premier
# 13/1/21
# Paulinette

def premier(val):
    prems = True
    div = 2
    while prems and div * div <= val:
        if val % div == 0:
            prems = False
        div += 1
    return prems


val = int(input("Entrez un nombre entier supérieur à 1 : "))
first = premier(val)
if first == True:
    print(val, "est un nombre premier")
else:
    print(val, "n'est pas un nombre premier")

