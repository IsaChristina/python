import sys
sys.path.append("C:/Users/900226/Desktop/exercicios/atividade_dupla/Trabalho2/")
from model.funcionarios import Funcionario


class Funcionario_db(Funcionario):

# //////////////////
# Cadastra no banco de dados

    def cadastrar_db(self, funcionario):

        self.cursor.execute(f"Insert into Funcionarios values (DEFAULT, '{funcionario['Cargo']}', "
                            f"{funcionario['Salario']}, {funcionario['Id_pessoal']})")

        self.conexao.commit()

# //////////////////
# Edita a informação no banco de dados

    def editar_db(self, funcionario):

        self.cursor.execute(f"Update Funcionarios Set Cargo = '{funcionario['Cargo']}', "
                            f"Salario = {funcionario['Salario']} where Id = {funcionario['Id']}")

        self.conexao.commit()

# //////////////////
# Deleta a informação do banco de dados

    def deletar_db(self, id):

        self.cursor.execute(f'Update Equipes set Pessoa_1 = NULL where Pessoa_1 = {id}')
        self.cursor.execute(f'Update Equipes set Pessoa_2 = NULL where Pessoa_2 = {id}')
        self.cursor.execute(f'Update Equipes set Pessoa_3 = NULL where Pessoa_3 = {id}')
        self.cursor.execute(f'Update Equipes set Pessoa_4 = NULL where Pessoa_4 = {id}')
        self.cursor.execute(f"Delete from Funcionarios where Id = {id}")

        self.conexao.commit()

        return True