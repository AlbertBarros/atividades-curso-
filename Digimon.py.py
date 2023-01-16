import random #Biblioteca de funções de aleatoriedade



class Digimon:  
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        self._nome = nome 
        self._especie = especie 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rápido"

#As classes abaixos atendem o requisito obrigatório Nº2 - Criar 3 subclasses de
#Digimon com base em seu tipo
class Anjo(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
    
        self._tipo = "Anjo"
        self._movimento = "Torpedo Arpão"

class Reptil(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "reptil"
        self._movimento = "Garra de Ataque"

class Aquatico(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Aquatico"
        self._movimento = "jato d'agua"

class Virus(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Virus"
        self._movimento = "Raio de choque"

class Ave(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Ave"
        self._movimento = "Asas de fogo"
class Alienígena(Digimon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Alienígena"
        self._movimento = "Vento veloz"

class Treinador: #Requisito Obrigatório #3 - Modelar classe Treinador
    def __init__(self, nome, Digimons):
        self._nome = nome
        self._Digimons = Digimons

    def escolherDigimon(self):
        return random.choice(self._Digimons)

#Requisito Obrigatório #4 - Modelar as subclasses Jogador e Inimigo
class Jogador(Treinador):
    def __init__(self, nome, Digimons):
        super().__init__(nome, Digimons)

    def escolherDigimon(self): #Requisitos Obrigatórios #5 e #8 - Esse método permite que o jogador escolha um Digimon de sua lista para batalhar
        while True:
            print(f"Escolha seu Digimon: ")

            for i in range(len(self._Digimons)):
                print(f"{i+1}. {self._Digimons[i]._nome}")

            DigimonEscolhido = input("Digite o número do Digimon escolhido: ")

            #return self._Digimons[int(DigimonEscolhido)-1] <<< Só precisa dessa linha

            #Esses ifs são extra
            if (DigimonEscolhido.isnumeric()):
                if (int(DigimonEscolhido) <= len(self._Digimons)):
                    return self._Digimons[int(DigimonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")

    def capturarDigimon(self, DigimonCapturado): #Requisito Obrigatório #6 - Essa função recebe o Digimon escolhido e adiciona a lista de Digimons do jogador
        self._Digimons.append(DigimonCapturado)
        print(f"Você capturou o {DigimonCapturado._nome}")
    
    def listarDigimons(self): # Requisito Obrigatório #7 - Essa função lista todos os Digimons presentes na lista de Digimons do jogador
        print("Sua lista de Digimon: ")
        for i in range(len(self._Digimons)):
                print(f"{i+1}. {self._Digimons[i]._nome}")

         

class Inimigo(Treinador):
    def __init__(self, nome, Digimons):
        super().__init__(nome, Digimons)


#Requisito Obrigatório #5 - A função abaixo recebe dois treinadores (Jogador e Inimigo) e invoca
#os métodos de escolha de Digimon de cada um. O Jogador pode escolher o próprio Digimon e o Inimigo
#escolhe um Digimon aleatório de sua lista. Os Digimons são salvos em duas variáveis e seus atributos
#são somados para compor uma nova variável chamada Força, o Digimon com a maior Força vence o duelo.
    
def batalhaDigimon(treinador1, treinador2): 

    p1 = treinador1.escolherDigimon()
    p2 = treinador2.escolherDigimon()

    p1Forca = (p1._ataque + p1._defesa + p1._hp) * random.randint(1,3)
    p2Forca = (p2._ataque + p2._defesa + p2._hp) * random.randint(1,3)

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e força {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")

DigimonsDisponiveis = [
Anjo("Angemon", "HolyAngemon", "Asas", 100,50,50),
Reptil("Agomon", "Greymon", "Vaccine",200,50,50),
Aquatico("Sabmarimon", "Armadimon", "Aquatico",300,50,50),
Virus("Zudomon", "VIKEMON", "Fogo", 200, 100, 100),
Ave ("Falcomon", "Diatrymon", "Falco Rush",300,50,50),
Alienígena("Vademon", "Ebemon", "Aquatico",300,100,50),
]

# Digimon1 = Fogo("Betinho", "Charmander", "Fogo", 100,50,50)
# Digimon2 = Grama("Verdinho", "Bulbasauro", "Grama",200,50,50)
# Digimon3 = Aquatico("Tortuguita", "Squirtle", "Aquatico",300,50,50)
nomeJogador = input("Digite seu nome: ")

print("Escolha seu Digimon inicial: ")

for i in range(3):
    print(f"{i+1}. {DigimonsDisponiveis[i]._nome}")

DigimonInicial = DigimonsDisponiveis[int(input("Digite o Digimon escolhido: "))-1]

print(f"O digimon escolhido foi o {DigimonInicial._nome}")

jogador = Jogador(nomeJogador, [DigimonInicial])
inimigo = Inimigo("Taichi Kamiya", DigimonsDisponiveis)

while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus Digimons
    2. Capturar um novo Digimon
    3. Batalhar contra outro Digimon
    4. ver evoluções dos Digimons
    0. Sair do jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Você saiu do jogo.")
        break
    elif menu=="1":
        jogador.listarDigimons()
    elif menu=="2":
        print("Escolha um Digimon para capturar: ")

        for i in range(len(DigimonsDisponiveis)):
            print(f"{i+1}. {DigimonsDisponiveis[i]._nome}")
        
        capturado = DigimonsDisponiveis[int(input("Digite o Digimon escolhido: "))-1]
        jogador.capturarDigimon(capturado)
    elif menu=="3":
        batalhaDigimon(jogador,inimigo)
    elif menu=="4":
        print ("Angemon evolui para HolyAngemon\n Agomon evolui para Greymon\n Sabmarimon evolui para Armadimon\n Zudomon evolui para VIKEMON\n Falcomon evolui para Diatrymon\n Vademon evolui para Ebemon")
    else:
        print("Você digitou algo inválido, tente novamente.")