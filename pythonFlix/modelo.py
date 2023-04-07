class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

avengers = Filme('vingadore guerra infinita', 2018, 160)
print(avengers.nome)



class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

theLastOfUs = Serie('the last of us', 2023, 160)
print(f'\n- Nome: {theLastOfUs.nome} \n- Ano: {theLastOfUs.ano} \n- Temporadas: {theLastOfUs.temporadas}')