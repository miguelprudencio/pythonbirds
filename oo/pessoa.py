class Pessoa:
    def comprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.comprimentar(p))
    print(p)
    print(p.comprimentar())