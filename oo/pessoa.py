class Pessoa:
    def __init__(self, *filho,nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filho = list(filho)

    def comprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    kelvem = Pessoa(nome='kelvem', idade=11)
    miguel = Pessoa(kelvem, nome='Miguel', idade=26)
    print(Pessoa.comprimentar(miguel))
    print(id(miguel))
    print(miguel.comprimentar())
    print(miguel.nome)
    print(miguel.idade)
    for filho in miguel.filho:
        print(filho.nome)


