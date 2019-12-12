from dao.conexao import Conexao

class Funcionario(Conexao):

# //////////////////
# Salva os dados de cadastro na classe
    def set_cadastrar(self, cargo, salario, id_pessoal):

        self.cargo = cargo
        self.salario = salario
        self.id_pessoal = id_pessoal

# Pega os dados da classe e transforma em um dicionario
    def get_cadastrar(self):

        return {'Cargo':self.cargo, 'Salario':self.salario, 'Id_pessoal':self.id_pessoal}

# //////////////////
# Salva os dados de edição na classe
    def set_editar(self, id, cargo, salario):

        self.id = id
        self.cargo = cargo
        self.salario = salario

# Pega os dados da classe e transforma em um dicionario
    def get_editar(self):

        return {'Id':self.id, 'Cargo':self.cargo, 'Salario':self.salario}

