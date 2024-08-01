import os
os.system("cls")
print("jogo da velha #")

jogadorX = input("Digite o nome do jogador X: ")
jogadorO = input("Digite o nome do jogador O: ")

jogadorO = jogadorO if jogadorO != "" else "jogador o"
jogadorX = jogadorX if jogadorX != "" else "jogador x"

dados = {
    # numero da partida
    "partida" : 1,
    # vez sai 1 ou 2
    "vez" : lambda x: "x" if x % 2 == 0 else "o",
    # nome dos jogadores
    "x" : jogadorX,
    "o" : jogadorO,
    # lista do jogo para apresentar
    "jogo" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # lista de para comparar durante o jogo
    "valor" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # valor da posição
    "pose" : 0,
    # mensagem gerada nas funções
    "mensagem" : "",
    # dinaliza o jogo parando o laço
    "final" : True
}

# print(dados["vez"](dados["partida"]))

# mostra como está a lista
def apresenta_hashtag(dado):
    # hashtag em lista com valor 1, 2, 3, 4, 5, 6, 7, 8, 9
        # 1 | 2 | 3
        # ----------
        # 4 | 5 | 6
        # ----------
        # 7 | 8 | 9
    forma = ""
    contador = 0
    for i in dado:
        contador += 1

        if contador == 3 or contador == 6:
            forma = f"{forma}{i}"
            print(forma)
            print("-------------")
            forma = ""
        elif contador == 9:
            forma = f"{forma}{i}"
            print(forma)
            forma = ""
        else:
            forma += f"{i}  | "

# para o laço no momento certo
def verificarVitoria(dado):
    # verifica se a posisção jogada é valida
    # verifica se coluna um coluna 2 ou coluna 3 tem o mesmo simbolo
    # verifica se linha um linha 2 ou linha 3 tem o mesmo simbolo
    # verifiva verticalmente
    # horizontal

    # 0 | 1 | 2
    # ----------
    # 3 | 4 | 5
    # ----------
    # 6 | 7 | 8
    if dado["jogo"][0] == dado["jogo"][1] and dado["jogo"][0] == dado["jogo"][2]:
        dado["jogo"][0].upper()
        dado["jogo"][1].upper()
        dado["jogo"][2].upper()
        dado["mensagem"] = "vitoria na linha 1"
        dado["final"] = False
    if dado["jogo"][3] == dado["jogo"][4] and dado["jogo"][3] == dado["jogo"][5]:
        dado["jogo"][3].upper()
        dado["jogo"][4].upper()
        dado["jogo"][5].upper()
        dado["mensagem"] = "vitoria na linha 2"
        dado["final"] = False
    if dado["jogo"][6] == dado["jogo"][7] and dado["jogo"][6] == dado["jogo"][5]:
        dado["jogo"][6].upper()
        dado["jogo"][7].upper()
        dado["jogo"][5].upper()
        dado["mensagem"] = "vitoria na linha 3"
        dado["final"] = False

    # vertical
    if dado["jogo"][0] == dado["jogo"][3] and dado["jogo"][0] == dado["jogo"][6]:
        dado["jogo"][0].upper()
        dado["jogo"][3].upper()
        dado["jogo"][6].upper()
        dado["mensagem"] = "vitoria na coluna 1"
        dado["final"] = False
    if dado["jogo"][1] == dado["jogo"][4] and dado["jogo"][1] == dado["jogo"][7]:
        dado["jogo"][1].upper()
        dado["jogo"][4].upper()
        dado["jogo"][7].upper()
        dado["mensagem"] = "vitoria na coluna 2"
        dado["final"] = False
    if dado["jogo"][2] == dado["jogo"][5] and dado["jogo"][2] == dado["jogo"][8]:
        dado["jogo"][2].upper()
        dado["jogo"][5].upper()
        dado["jogo"][8].upper()
        dado["mensagem"] = "vitoria na coluna 3"
        dado["final"] = False

    # agonal
    if dado["jogo"][0] == dado["jogo"][4] and dado["jogo"][0] == dado["jogo"][8]:
        dado["jogo"][0].upper()
        dado["jogo"][4].upper()
        dado["jogo"][8].upper()
        dado["mensagem"] = "vitoria deagonal casa 1, 5 e 9"
        dado["final"] = False
    if dado["jogo"][2] == dado["jogo"][4] and dado["jogo"][2] == dado["jogo"][6]:
        dado["jogo"][2].upper()
        dado["jogo"][4].upper()
        dado["jogo"][6].upper()
        dado["mensagem"] = "vitoria deagonal casa 3, 5 e 7"
        dado["final"] = False
    # verifica se lista jogo tem o uma casa vazia para continuar
    vazio = 0
    for i in dado["jogo"]:
        if i in dado["valor"]:
            vazio += 1
    if vazio < 1:
        dado["mensagem"] = "velhou"
        dado["final"] = False
    
    return dado

# pose unico input durante o jogo
def tratarInput(dado,pose):
    dado["mensagem"] = ""
    # tratamento
    try:
        dado["pose"] = int(pose) - 1
        # verifica casa ocupada
        # if pose == "X" or pose == "O":
        if dado["jogo"][dado["pose"]] == dado["vez"](1) or dado["jogo"][dado["pose"]] == dado["vez"](2):
            dado["mensagem"] = f"casa {pose} ocupada por: {dado["jogo"][dado["pose"]]} "
        else:
            dado["mensagem"] = "boa jogada"
            # nesse caso foi atribuido o valor a casa desse dado
            dado["jogo"][dado["pose"]] = dado["vez"](dado["partida"])
            dado["partida"] += 1
            return verificarVitoria(dado)
    except ValueError:
        # apresentar erro
        dado["mensagem"] = f"Valor (\' {pose} \') invalido"
    
    return verificarVitoria(dado)

def partida(dado):
    while dado["final"]:
        os.system("cls")
        apresenta_hashtag(dado["jogo"])
        print(f"jogada: {dado["partida"]}")
        print(f"Mensagem: {dado["mensagem"]}")
        # pede os dados da posição do jogador da vez
        pose = input(f"Vez de {dado[dado["vez"](dado["partida"])]} {dado["vez"](dado["partida"])}: ")
        dado = tratarInput(dado, pose)
    # acaba o jogo
    os.system("cls")
    print("Fim de jogo")
    apresenta_hashtag(dado["jogo"])
    print(dado["mensagem"])

partida(dados)