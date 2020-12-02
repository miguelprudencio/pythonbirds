class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Miguel', 26)
    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'francisco'
    p.idade = 40
    print(p.nome)
    print(p.idade)
