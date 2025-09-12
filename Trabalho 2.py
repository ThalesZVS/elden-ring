import requests
def wiki_dos_bosses():
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
    print("Digite 1 ")
    Escolha2 = int(input())
    if Escolha2 == 1:
        Wiki_dos_locais()
    elif Escolha2 == 0:
        menu_inicial()
    while True:
        Escolha = input("Escolha um local: ")
        encontrado = False

        for local in locais:
            if Escolha == local["name"]:
                print(local["description"])
                encontrado = True
                break

        if encontrado:
          menu_inicial()
        else:
            print("Local não encontrado. Por favor, tente novamente.")
def Wiki_dos_locais():
    Url = "https://eldenring.fanapis.com/api/bosses"
    Response = requests.get(Url)
    print(Response)
    Dados = Response.json()
    Criaturas = Dados["data"] 
    for Bosses in Criaturas:
        print (Bosses["name"])
    Escolha = input("Escolha um Boss ")
    for Bosses in Criaturas:
        if Escolha == Bosses["name"]:
            print(Bosses["description"])
            print("Digite 2 ")
            Escolha2 =int(input())
            if Escolha2 == 2:
                wiki_dos_bosses()
            elif Escolha2 == 0:
                menu_inicial()
    while True:
        Escolha = input("Escolha um Boss")
        encontrado = False

        for Bosses in Criaturas:
            if Escolha == Bosses["name"]:
                print(Bosses["description"])
                encontrado = True
                break

        if encontrado:
            break  # Sai do loop se encontrou o local
        else:
            print("Local não encontrado. Por favor, tente novamente.")
def menu_inicial():
    print("=== Bem-vindo a EldenWiki! ===")
    while True:
        print("\nEscolha com o que deseja começar:")
        print(" 1 → Descobrir Localizações")
        print(" 2 → Descobrir Bosses")
        print(" 0 → Sair")
        escolha = input("Digite sua opção (1/2/0): ")

        if escolha == "1":
           wiki_dos_bosses()
        elif escolha == "2":
           Wiki_dos_locais()
        elif escolha == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução principal
if __name__ == "__main__":
    menu_inicial()

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
