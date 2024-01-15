from pprint import pprint

from pymongo import MongoClient

client = MongoClient("mongodb+srv://usuario:<SENHA>@cluster0.gc1haei.mongodb.net/?retryWrites=true&w=majority")

db = client.banco

clientes = db.clientes

registro_de_clientes = [
    {"Nome": "Felipe Rodrigues Fonseca",
     "Cpf": 2123487234,
     "Endereço": 'Rua Jardim Flores Nº 35 B. Centro',
     "Conta": [{"Tipo": "Salário", "Agência": 33, "Número": 32421312, "Saldo": 0}]
     },
    {"Nome": "Luigi Gomes Fonseca",
     "Cpf": 2325435345,
     "Endereço": "Rua Gerenal Estíbal Nº4 B. Centro",
     "Conta": [{"Tipo": "Salário", "Agência": 33, "Número": 4534523, "Saldo": 0},
               {"Tipo": "Corrente", "Agência": 33, "Número": 6575632, "Saldo": 0}]
     }
]


# =-=-=-=-=-=- Persistindo dados no Banco de dados =-=-=-=-=-=-=-=
resultado = clientes.insert_many(registro_de_clientes).inserted_ids

# =-=-=-=-=-=- Resultados e Prints =-=-=-=-=-=-=-=

print("====> Obtendo inserted Ids\n")
pprint(f"{clientes.inserted_ids}")
print()
print("====> Obtendo dados com Find_One\n")
pprint(f"{db.clientes.find_one()}")
print()
print("====> Obtendo dados com Find_One usando um nome como filtro\n")
pprint(f"{db.clientes.find_one({'Nome':'Luigi Gomes Fonseca'})}")
print()
print("====> Obtendo todos os dados cadastrados\n")
for registros in clientes.find():
    pprint(registros)

print()
print("====> Obtendo a quantidade de dados persistidos")
print(clientes.count_documents({}))

print()
print("====> Obtendo todos os dados cadastrados de forma ordenada pelo nome\n")
for registros in clientes.find({}).sort("Nome"):
    pprint(registros)

print()
print("====> Obtendo todas as coleções\n")
collections = db.list_collection_names()
print(collections)
