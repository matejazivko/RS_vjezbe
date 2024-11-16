
def filtriraj_parne(lista):
   parni = [a for a in lista if a % 2 == 0]
   return parni

lista = [1,2,3,4,5,6,7,8,9,10] 

print (filtriraj_parne(lista))
    