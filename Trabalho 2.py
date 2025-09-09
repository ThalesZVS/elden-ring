import requests
Url = "https://eldenring.fanapis.com/api/locations"
Response = requests.get(Url)
print(Response)
Dados = Response.json()
locais = Dados["data"]
for local in locais:
    print (local["name"])
Escolha = input("Escolha um local ")
for local in locais:
    if Escolha == local["name"]:
        print(local["description"])
while True:
    Escolha = input("Escolha um local: ")
    encontrado = False

    for local in locais:
        if Escolha == local["name"]:
            print(local["description"])
            encontrado = True
            break

    if encontrado:
        break  # Sai do loop se encontrou o local
    else:
        print("Local não encontrado. Por favor, tente novamente.")


    #codigo perfeito onde ele entrega os locais e para quando nao tem mais oq entregar sem erro.
    #print(Dados)
    #print(Dados["data"][2]["name"]) #se eu quiser de todos eu faço um loppy
    
    #A = 1
    #while True:
    #print(Dados["data"][A]["name"])
    #A =A+1 #assim ele vai funcionar mais vai falar que esta errado pois vai ir ate falhar. portanto vc tem que fazer uma continuaçao para que ele tenha um limite.
    #nesse momento estou tentando colocar para se a pessoa escrever errado o o codigo fazer um loop ate a pessoa acertar. o professor
    #falou um jeito usand
    #"def localizar()"
    #A = imput 
        #for
            #if
    #localizar()
    #na logica essa seria uma estrutura legal... mas eu quero na minha cabeça teimosa eu poderia usar o while
   
