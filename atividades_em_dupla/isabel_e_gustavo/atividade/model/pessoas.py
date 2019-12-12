from dao.conexao import Conexao

class Pessoa(Conexao):

# //////////////////
# Salva os dados de cadastro na classe
    def set_cadastrar(self, nome, cpf, telefone):

        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

# Pega os dados da classe e transforma em um dicionario
    def get_cadastrar(self):

        return {'Nome':self.nome, 'Cpf':self.cpf, 'Telefone':self.telefone}

# //////////////////
# Salva os dados de edição na classe
    def set_editar(self, id, nome, cpf, telefone):

        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

# Pega os dados da classe e transforma em um dicionario
    def get_editar(self):

        return {'Id':self.id, 'Nome':self.nome, 'Cpf':self.cpf, 'Telefone':self.telefone}

