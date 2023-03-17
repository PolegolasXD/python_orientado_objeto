class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")

        return self.__nome.title()
    
    #__nome, "private"
    #@property, acessar metodo sem "()"
    #
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()") 
        self.__nome = nome

        #chamando a propriedade setter sem () e sem __set__ no metodo
        