def ukloni_duplikate(lista):
    duplikati = list(set(lista))
    return duplikati

lista = [1,2,3,4,5,1,2,3,4,5] 
print(ukloni_duplikate(lista))