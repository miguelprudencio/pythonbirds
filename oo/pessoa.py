class Pessoa:
    olhos=2
    def __init__(self, *filho,nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filho = list(filho)
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} -- olhos {cls.olhos}'

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
    miguel.sobrenome = 'Prudencio'
    print(miguel.sobrenome)
    miguel.olhos = 1
    print(miguel.__dict__)
    print(kelvem.__dict__)
    print(id(Pessoa.olhos), id(miguel.olhos), id(kelvem.olhos))
    print(Pessoa.metodo_estatico())
    print(miguel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), miguel.nome_e_atributos_de_classes())

