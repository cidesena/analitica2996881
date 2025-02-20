# lista=[]

# for i in range(11):
#     lista.append(i*10)

# print(lista)

def llenarListaFactorDiez(lista,cantidad):
    lista=[]
    for i in range(cantidad):
        lista.append(i*10)
    return lista

def llenarLista(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=int(input("ingrese numero"))
        lista.append(num)
    return lista

vector=[]
vector=llenarLista(vector,5)
print(vector)
# print("-"*20)
# llenarLista(10)
# print("-"*20)
# llenarLista(20)
