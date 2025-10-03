import requests
def Wiki_dos_locais():
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
            print("Nome do local: " + local["name"])
            print("Descrição do local: " + local["description"])
            print("Região localizada: " + local["region"])
    print("Digite 1 para continuar o 0 para sair para o menu inicial.")
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
def wiki_dos_bosses():
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
            print("Nome da creatura: " + Bosses["name"])
            print("Descrição da creatura: " + Bosses["description"])
            print("localização da espécie: " + Bosses["location"])
            print("Items dropados pela creatura: ")
            print(Bosses["drops"])
            print("Digite 2 para continuar ou 0 para sair para o menu inicial.")
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
        print(" 3 → Descobrir Criaturas")
        print(" 4 → Descobrir Npcs")
        print(" 5 → Descobrir armas")
        print(" 6 → Descobrir classes")
        print(" 0 → Sair")
        escolha = input("Escolha uma funçâo (1/2/3/4/5/6/0): ")

        if escolha == "1":
           Wiki_dos_locais()
        elif escolha == "2":
           wiki_dos_bosses()
        elif escolha == "3":
            wiki_das_criaturas()
        elif escolha == "4":
            wiki_dos_npcs()
        elif escolha == "5":
            wiki_da_armas()      
        elif escolha == "6":
            wiki_das_classes()      
        elif escolha == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def wiki_das_criaturas():
    Url = "https://eldenring.fanapis.com/api/creatures"
    Response = requests.get(Url)
    print(Response)
    Dados = Response.json()
    especies = Dados["data"]
    for especime in especies:
        print (especime["name"])
    Escolha = input("Escolha uma Criatura ")
    for especime in especies:
        if Escolha == especime["name"]:
            print("Nome da creatura: " + especime["name"])
            print("Descrição da creatura: " + especime["description"])
            print("localização da espécie: " + especime["location"])
            print("Items dropados pela creatura: ")
            print(especime["drops"])

            print("Digite 3 para continuar ou 0 para sair para o menu inicial.")
            Escolha2 =int(input())
            if Escolha2 == 3:
                wiki_das_criaturas()
            elif Escolha2 == 0:
                menu_inicial()
    while True:
        Escolha = input("Escolha uma Criatura ")
        encontrado = False
        for especime in especies:
            if Escolha == especime["name"]:
                print(especime["description"])
                encontrado = True
                break

def wiki_dos_npcs():
    Url = "https://eldenring.fanapis.com/api/npcs"
    Response = requests.get(Url)
    print(Response)
    Dados = Response.json()
    Npcs = Dados["data"]
    for npc in Npcs:
        print (npc["name"])
    Escolha = input("Escolha um npc ")
    for npc in Npcs:
        if Escolha == npc["name"]:
            print("Nome: " + npc["name"])
            print("Função no mundo: " + npc["role"])
            print("Localização: " + npc["location"])
            print("Digite 4 para continuar ou 0 para sair para o menu inicial.")
            Escolha2 =int(input())
            if Escolha2 == 4:
                wiki_dos_npcs()
            elif Escolha2 == 0:
                menu_inicial()
    while True:
          Escolha = input("Escolha um npc ")  
          encontrado = False
          for npc in Npcs:
              if Escolha == npc["name"]:
                  print(npc["role"])
                  encontrado = True
                  break
def wiki_da_armas():
    Url = "https://eldenring.fanapis.com/api/weapons"
    Response = requests.get(Url)
    print(Response)
    Dados = Response.json()
    armas = Dados["data"]
    for arma in armas:
        print (arma["name"])
    Escolha = input("Escolha uma arma ")
    for arma in armas:
        if Escolha == arma["name"]:
            print ("Nome da classe: " + arma["name"])
            print("Descrisão da Arma: " + arma["description"])
            print("Estatísticas da arma: ")
            print(arma["attack"])
            print("Digite 5 para continuar ou 0 para sair para o menu inicial. ")
            Escolha2 =int(input())
            if Escolha2 == 5:
                wiki_da_armas()
            elif Escolha2 == 0:
                menu_inicial()
    while True:
          Escolha = input("Escolha uma arma ") 
          encontrado = False
          for arma in armas:
              if Escolha == arma["name"]:
                  print(arma["name"])
                  encontrado = True
                  break
def wiki_das_classes():
    Url = "https://eldenring.fanapis.com/api/classes"
    Response = requests.get(Url)
    print(Response)
    Dados = Response.json()
    classes = Dados["data"]
    for classe in classes:
        print (classe["name"])
    Escolha = input("Escolha uma classe ")
    for classe in classes:
        if Escolha == classe["name"]:
            print ("Nome da classe: " + classe["name"])
            print("Descrisão da classe: " + classe["description"])
            print("Estatísticas da classe: ")
            print(classe["stats"])
            print("Digite 6 para continuar ou 0 para sair para o menu inicial. ")
            Escolha2 =int(input())
            if Escolha2 == 5:
                wiki_das_classes()
            elif Escolha2 == 0:
                menu_inicial()
    while True:
          Escolha = input("Escolha uma classe ") 
          encontrado = False
          for classe in classes:
              if Escolha == classe["name"]:
                  print(classe["name"])
                  encontrado = True
                  break
# Execução principal
if __name__ == "__main__":
    menu_inicial()
    #ir  atras de fazer uma nova funçao onde se tem uma builds prontas e uma forma de o sistema fazer uma build aleatoria... como seria muito desbalanceado da pra
    #a build que voce recebesse aleatoria poderia tem algum buff desde drop ou loot
    #e ir atras de guarda-la em um arquivo txt com aquele codigo que o professor passou... mas talves nao.
