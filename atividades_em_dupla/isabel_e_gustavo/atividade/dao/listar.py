from dao.conexao import Conexao

class Listar(Conexao):

# //////////////////
# Lista todas as pessoas do banco de dados
    def listar_pessoas(self):

        lista = []

        self.cursor.execute('Select * from Pessoas')

        for i in self.cursor.fetchall():
            lista.append({'Id': i[0], 'Nome': i[1],
                          'Cpf': i[2], 'Telefone': i[3]})

        return lista

# //////////////////
# Lista todos os funcionários do banco de dados

    def listar_funcionarios(self):

        lista = []

        self.cursor.execute('Select * from Funcionarios')

        for i in self.cursor.fetchall():
            lista.append({'Id': i[0], 'Cargo': i[1],
                          'Salario': i[2], 'Id_pessoal': i[3]})

        return lista

# //////////////////
# Lista todas as equipes do banco de dados

    def listar_equipes(self):

        lista = []

        self.cursor.execute('Select * from Equipes')

        for i in self.cursor.fetchall():
            lista.append(
                {'Id': i[0], 'Pessoa_1': i[1], 'Pessoa_2': i[2], 'Pessoa_3': i[3], 'Pessoa_4': i[4]})

        return lista

# //////////////////
# Lista todas as linguagens do banco de dados

    def listar_linguagens(self):

        lista = []

        self.cursor.execute('Select * from Linguagens')

        for i in self.cursor.fetchall():
            lista.append({'Id': i[0], 'Nome': i[1]})

        return lista

# //////////////////
# Lista um funcionário e a pessoa específicos

    def funcionario_individual(self, id):

        self.cursor.execute(f'Select * from Pessoas where Id = {id}')

        l1 = self.cursor.fetchone()

        self.cursor.execute(
            f'Select * from Funcionarios where Id_pessoal = {id}')

        l2 = self.cursor.fetchone()

        return {'Id_pessoal': l1[0], 'Nome': l1[1], 'Cpf': l1[2], 'Telefone': l1[3], 'Id_funcionario': l2[0], 'Cargo': l2[1], 'Salario': l2[2]}

# Lista uma equipe específica
    def equipe_individual(self, id):

        self.cursor.execute(f'Select * from Equipes where Id = {id}')

        i = self.cursor.fetchone()

        return {'Id_equipe': i[0], 'Pessoa_1': i[1], 'Pessoa_2': i[2], 'Pessoa_3': i[3], 'Pessoa_4': i[4]}

# Lista uma linguagem específica
    def linguagem_individual(self, id):

        self.cursor.execute(f'Select * from Linguagens where Id = {id}')

        i = self.cursor.fetchone()

        return {'Id':i[0], 'Nome':i[1]}
