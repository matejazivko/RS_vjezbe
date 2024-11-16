#1
lista = [1,2,3,4,5,6,7,8,9,10]
def prvi_i_zadnji(lista):
    return(lista[0], lista[9])
print(prvi_i_zadnji(lista))



#3
skup_1 = {1,2,3,4,5}
skup_2 = {4,5,6,7,8}
def presjek (skup_1,skup_2):
        return skup_1.intersection(skup_2)
print(presjek(skup_1,skup_2))

