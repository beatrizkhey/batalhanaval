import random
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")

cls()

# Constantes
QTD_NAVIOS     = 3 
QTD_SUBMARINOS = 2
QTD_POSTOS     = 2

PTS_NAVIOS     = 5
PTS_SUBMARINOS = 7

AGUA_NEV      = 0
NAVIO_NEV     = 1
SUBMARINO_NEV = 2
POSTO_NEV     = 3
NAVIO         = 4
SUBMARINO     = 5
POSTO         = 6
AGUA_ATINGIDA = 7

# Variáveis globais
global dim
global marInimigo
global disparos
global qtdD
global qtdN
global qtdS
global qtdD_tempo
global msg
global tipo
global quantidade
global nome
global totalPontos
global controle
global msgfim

dim = 10
marInimigo = [] 
disparos = []
qtdD = 0
qtdN = 0    
qtdS = 0    
qtdD_tempo = 0
msg = "Início do jogo! Boa sorte!\n"
msgfim = "Fim de jogo!"
tipo = 0
quantidade = 0
nome = ''
totalPontos = 0
controle = 1

# Função 1
def iniciaMarInimigo():
    '''
    Inicializa a matriz marInimigo[10][10] e preenche com AGUA_NEV = 0
    :param: none
    :return: none
    '''
    global marInimigo
    marInimigo = []

    for i in range(dim):
        marInimigo.append([])
        for j in range(dim):
            marInimigo[i].append(AGUA_NEV)

    posicionaElemento(NAVIO_NEV, QTD_NAVIOS)
    posicionaElemento(POSTO_NEV, QTD_POSTOS)
    posicionaElemento(SUBMARINO_NEV, QTD_SUBMARINOS)

# Função 2
def posicionaElemento(tipo, quantidade):
    '''
    Posiciona aleatoriamente elementos no marInimigo[10][10]. 
    A função tenta posicionar o elemento em coordenadas aleatórias X e Y.
    Se a função, ao tentar posicionar um elemento em coordenadas aleatórias X e Y,
    encontrar a posição preenchida com 1, 2 ou 3 para navio, submarino ou posto (respectivamente),
    deve tentar outras coordenas aleatórias X e Y para posicionar novamente, até encontrar a posição vazia (com 0, que indica água).
    :param tipo: Valor do tipo de elemento (navio = 1, submarino = 2 ou posto = 3)
    :param quantidade: Quantidade de elementos de cada tipo a ser preenchido
    :return: none
    '''
    global marInimigo
    while quantidade > 0:
        i = random.randint(0,9)                
        j = random.randint(0,9)
        if marInimigo[i][j] == AGUA_NEV:
            marInimigo[i][j] = tipo
            quantidade -= 1
        
# Função 3
def tipoElemento(codigoTipo):
    '''
    Recebe um código de um elemento e retorna seu símbolo (caractere) correspondente.
    :param codigoTipo: matriz com coordenadas do marInimigo
    :return: retorna o caractere correspondente a cada codigoTipo
    '''
    if codigoTipo == AGUA_NEV:
        return "."
    if codigoTipo == NAVIO_NEV:
        return "."
    if codigoTipo == SUBMARINO_NEV:
        return "."
    if codigoTipo == POSTO_NEV:
        return "."
    if codigoTipo == NAVIO:
        return "N"
    if codigoTipo == SUBMARINO:
        return "S"
    if codigoTipo == POSTO:
        return "P"
    if codigoTipo == AGUA_ATINGIDA:
        return "%"

# Função 4
def exibeMarinimigo():
    '''
    Varre (percorre) a matriz e, dependendo do valor encontrado na matriz, a função exibe seu respectivo símbolo (., %, N, S ou P).
    :param: none
    :return: none
    '''    
    print("    ", end="")
    for index in range (10):        
        print(f" [{index}]", end = "") 
    print("\n    +---+---+---+---+---+---+---+---+---+---+")
    
    for i in range(10):
        print(f"[{i}] |", end = "")
        for j in range(10):
            simbolo = tipoElemento(marInimigo[i][j])
            print(f"{simbolo:^3}|", end= "")
        print("\n    +---+---+---+---+---+---+---+---+---+---+")

# Função 5
def nomepiloto():
    '''
    Solicita ao usuário o nome do piloto; faz tratamento de exceção no caso de caractere inválido (^Z, ^C etc)
    :param: none
    :return: String com o nome do piloto
    '''
    while True:
        try:
            global nome 
            nome = str(input("Digite o nome do piloto: "))
            break
        
        except:
            print("\n Erro de digitação! Digite qualquer tecla para continuar com o programa.")       
            input()
            cls()
    
    return nome

# Função 6
def inicializaJogo():
    '''
    Inicializa os valores da variáveis globais para novo jogo.
    :param: none
    :return: none
    '''
    # Variáveis globais
    global dim
    global marInimigo
    global disparos
    global qtdD
    global qtdN
    global qtdS
    global qtdD_tempo
    global msg
    global tipo
    global quantidade
    global nome
    global totalPontos
    global controle
    global retorno

    dim = 10
    marInimigo = [] 
    disparos = []
    qtdD = 0
    qtdN = 0    
    qtdS = 0    
    qtdD_tempo = 0
    msg = "Início do jogo! Boa sorte!\n"
    tipo = 0
    quantidade = 0
    nome = ''
    totalPontos = 0
    controle = 1
    retorno = 1

# Função 7
def apresentaTela(nomePiloto):
    '''
    Limpa a tela de console (cls), posiciona cabeçalho com destaque para o nome do piloto,
    chama a função exibeMarInimigo(), e apresenta as variáveis globais: qtdN, qtdS, qtdD, msg e totalPontos.
    :param nomePiloto: string com o nome do piloto
    :return: none
    '''
    cls()
    global msg
    global qtdD
    global qtdN
    global qtdS
    global totalPontos

    #Printa o radar
    print(45*"=")
    print(f"Ataque Aéreo, piloto: {nomePiloto}")
    print(45*"=")
    print("    ", end = "")
    print()

    #Printa o marInimigo
    exibeMarinimigo()

    #Printa o cabeçalho
    print(f"Disparos realizados: {qtdD}")
    print(f"Navios atingidos: {qtdN}")
    print(f"Submarinos atingidos: {qtdS}")
    print(f"Total de pontos: {totalPontos}")
    print()
    print(msg)

# Função 8
def verificaDisparo(coord):
    ''' 
    Verifica o valor do elemento encontrado nas coordenadas X e Y do mar inimigo (marInimigo[x][y]) e,
    dependendo desse valor, altera as variáveis globais qtdN, qtdS, qtdD e msg.
    :param coord: coordenada do disparo    
    :return: 1 (continua o jogo) e 0 (termina o jogo)
    '''
    global msg
    global qtdD
    global qtdN
    global qtdS
    global qtdD_tempo
    global totalPontos
    global disparos
    global msgfim

    qtdD += 1
    qtdD_tempo += 1

    try:
        if marInimigo[coord[0]][coord[1]] == AGUA_NEV:
            msg = "SPLASH! Caiu na água"
            marInimigo[coord[0]][coord[1]] = AGUA_ATINGIDA
            return 1

        if marInimigo[coord[0]][coord[1]] == NAVIO_NEV:
            msg = "BOOM! Navio atingido!"
            qtdN += 1
            totalPontos += 5
            marInimigo[coord[0]][coord[1]] = NAVIO
            return 1

        if marInimigo[coord[0]][coord[1]] == SUBMARINO_NEV:
            msg = "BOOM! Submarino atingido!"
            qtdS += 1
            totalPontos += 7
            marInimigo[coord[0]][coord[1]] = SUBMARINO
            return 1

        if marInimigo[coord[0]][coord[1]] == POSTO_NEV:
            msg = "BOOM! Posto atingido! Você foi eliminado!!!"
            marInimigo[coord[0]][coord[1]] = POSTO
            return 0
        
        if marInimigo[coord[0]][coord[1]] == AGUA_ATINGIDA:
            msg = "SPLASH! Caiu na água"        
            return 1

        if marInimigo[coord[0]][coord[1]] == NAVIO:
            msg = "CRASH! Caiu nos destroços de navio!"        
            return 1 

        if marInimigo[coord[0]][coord[1]] == SUBMARINO:
            msg = "CRASH! Caiu nos destroços de submarino!"
            return 1

        if (qtdN == QTD_NAVIOS) and (qtdS == QTD_SUBMARINOS):
            msg = "Você venceu!"
            return 0
           
    except:
        print("Valor inválido, tente novamente!")
        input()

# Função 9  
def jogo(nomePiloto):
    '''
    Executa o jogo, solicitando as coordenadas x e y do usuário. Verifica se as coordenasdas inseridas estão entre 0 e 9 (inclusive).
    Adiciona as coordenada inseridas à uma lista com as coordenadas a serem atacadas.
    Faz tratamento de exceção na leitura das coordenadas x e y caso seja inserido um valor inválido.
    Ao fim do jogo pergunta se deseja iniciar um novo jogo. Caso sim, limpa a tela e inicia novo jogo. Caso não, encerra o jogo.
    Faz tratamento de exceção caso seja inserida uma opção inválida (diferente de 's' e 'n')
    :param nomePiloto: Nome do piloto.
    :return: none
    '''
    global disparos
    global retorno
    
    while True:
        try:
            cls()
            apresentaTela(nomePiloto)
            disparo_t = []

            if retorno == 1:
                x = int(input("Insira uma coordenada X para realizar o disparo: "))
                y = int(input("Insira uma coordenada Y para realizar o disparo: "))
                
                if (0 <= x <= 9) and (0 <= y <= 9):
                    disparo_t.append(x)
                    disparo_t.append(y)
                    retorno = verificaDisparo(disparo_t)
                    print(msg)
                    
                else:
                    print("Valor Inválido!")
                    input()
                    retorno = 1
                
            else:
                continuar = str(input("Gostaria de reiniciar o jogo? (s/n) "))
                
                if continuar == "s":
                    cls()
                    inicializaJogo()
                    iniciaMarInimigo()
                    nomepiloto()
                    continue
                
                elif continuar == "n":
                    print("Fim de jogo!")
                    break
                
                else:
                    print("Resposta inválida, tente novamente!")
                    input()
                    continue
        
        except ValueError:
            print("Valor inválido, tente novamente!")
            input("Tecle <ENTER> para continuar.")
            continue
        except:
            print("Valor inválido, tente novamente!")
            input("Tecle <ENTER> para continuar.")
            continue          

# Executa o programa 
inicializaJogo()
iniciaMarInimigo()
nomepiloto()         
jogo(nome)