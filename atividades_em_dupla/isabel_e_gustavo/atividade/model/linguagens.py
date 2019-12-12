from dao.conexao import Conexao

class Linguagem(Conexao):

# //////////////////
# Salva os dados de cadastro na classe
    def set_cadastrar(self, nome):

        self.nome = nome

# Pega os dados da classe e transforma em um dicionario
    def get_cadastrar(self):

        return self.nome

# //////////////////
# Salva os dados de edição na classe
    def set_editar(self, id, nome):

        self.id = id
        self.nome = nome

# Pega os dados da classe e transforma em um dicionario
    def get_editar(self):

        return {'Id':self.id, 'Nome':self.nome}

