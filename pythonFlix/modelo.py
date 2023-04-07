class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

        
avengers = Filme('\n- vingadore guerra infinita', 2018, 160)
theLastOfUs = Serie('the last of us', 2023, 160)

avengers.dar_like()
theLastOfUs.dar_like()

print(f'\n- Nome: {avengers.nome} \n- Ano: {avengers.ano} \n- Temporadas: {avengers.duracao} \n- Likes: {avengers.likes}')
print(f'\n- Nome: {theLastOfUs.nome} \n- Ano: {theLastOfUs.ano} \n- Temporadas: {theLastOfUs.temporadas} \n- Likes: {theLastOfUs.likes}')
