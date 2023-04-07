class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


avengers = Filme('\n- vingadore guerra infinita', 2018, 160)


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

        

theLastOfUs = Serie('the last of us', 2023, 160)

avengers.dar_like()
theLastOfUs.dar_like()


print(f'\n- Nome: {avengers.nome} \n- Ano: {avengers.ano} \n- Temporadas: {avengers.duracao} \n- Likes: {avengers.likes}')
print(f'\n- Nome: {theLastOfUs.nome} \n- Ano: {theLastOfUs.ano} \n- Temporadas: {theLastOfUs.temporadas} \n- Likes: {theLastOfUs.likes}')
