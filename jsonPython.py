import json

jsonClients =  open('datos.json')
jsonClientsDic = open('datosDict.json')
cadenaJsonClientes = json.load(jsonClients)
dicJsonClientes = json.load(jsonClientsDic)

class client:
    def __init__(self,id,name,accountBalance):
        self._AccountBalance = accountBalance
        self._Id = id
        self._Name = name
    def setAccountBalance(self,quantity):
        self._AccountBalance = quantity
    def setName(self,name):
        self._Name = name
    def getAccountBalance(self):
        return self._AccountBalance
    def getName(self):
        return self._Name
    def getId(self):
        return self._Id

#precondición: recibir un string de la lista de clientes en notacion json
#Regresa una lista de objetos clientes.
def instantiateClients(jsonClientes):
    listaClientes = []
    for c in jsonClientes["clientList"]:
        id = c["id"]
        name = c["clientName"]
        balance = c["accountBalance"]
        listaClientes.append(client(id,name,balance))
    return listaClientes

def instantiateClients2(jsonClients):
    dictionaryClientes = {}
    for i,j in jsonClients.items():
        id = j["id"]
        clientName = j["clientName"]
        acBalance = j["accountBalance"]
        dictionaryClientes[int(id)] = client(int(id),clientName,acBalance)
    return dictionaryClientes

def getClientFromJson(jsonClients,id):
    return jsonClients[id]

#con instanciacion de objetos clientes, mayor seguridad, más lineas de código
x = instantiateClients2(dicJsonClientes).items()
for i,y in x:
    print(i,y.getName())


#sin usar la clase clientes, modificando directamente al archivo
client = getClientFromJson(dicJsonClientes,"0003")
print(client)
client["accountBalance"] -= 1000
print(client)
with open ("datosDict.json","w") as outfile:
    json.dump(dicJsonClientes,outfile)
