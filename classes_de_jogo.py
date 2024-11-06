class Heroi:
    def __init__(self, nome, idade, tipo):
        assert tipo in ("mago", "guerreiro", "monge", "ninja"), 'Você deve escolher um dos seguintes tipos: "mago", "guerreiro", "monge", "ninja"'

        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.xp = 0
        self.vitorias = 0
        self.derrotas = 0

        if tipo == "mago":
            self.ataque = "magia"
        elif tipo == "guerreiro":
            self.ataque = "espada"
        elif tipo == "monge":
            self.ataque = "artes marciais"
        elif tipo == "ninja":
            self.ataque = "shuriken"

    def atacar(self):
        print(f"o {self.tipo} atacou usando {self.ataque}")

    @property
    def saldo_vitorias(self):
        return self.vitorias - self.derrotas

    @property
    def nivel(self):
        saldo = self.saldo_vitorias

        if saldo <= 10:
            return "Ferro"
        elif saldo <= 20:
            return "Bronze"
        elif saldo <= 50:
            return "Prata"
        elif saldo <= 80:
            return "Ouro"
        elif saldo <= 90:
            return "Diamante"
        elif saldo <= 100:
            return "Lendário"
        return "Imortal"


nome = input("Digite o nome do herói: ")
idade = input("Digite a idade do herói: ")
tipo = input('Digite o tipo do herói ("mago", "guerreiro", "monge", "ninja"): ')

heroi = Heroi(nome, idade, tipo)

print()

while input("Deseja enfrentar um monstro (s/n): ") == "s":
    nivel_do_monstro = int(input("Qual o nível do monstro? "))
    nivel_de_dificuldade = int(input("Qual o nível de dificuldade? "))
    nivel_da_batalha = nivel_do_monstro * nivel_do_monstro * 100

    heroi.atacar()

    if heroi.xp >= nivel_da_batalha - 1000:
        heroi.vitorias += 1
        heroi.xp += nivel_da_batalha

        print("**Vitória**")
        print("XP:", heroi.xp)
    else:
        heroi.derrotas += 1

        print("**Derrota**")
    
    print(f"Vitórias: {heroi.vitorias}   Derrotas: {heroi.derrotas}")
    print()

print(f"O Herói **{heroi.nome}** tem de saldo de vitórias de **{heroi.saldo_vitorias}** e está no nível **{heroi.nivel}**")
