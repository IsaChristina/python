from model.linguagens import Linguagem


class Linguagem_db(Linguagem):

# //////////////////
# Cadastra no banco de dados

    def cadastrar_db(self, linguagem):

        self.cursor.execute(f"Insert into Linguagens values (DEFAULT, '{linguagem}')")

        self.conexao.commit()

# //////////////////
# Edita a informação no banco de dados

    def editar_db(self, linguagem):

        self.cursor.execute(f"Update Linguagens Set Nome = '{linguagem['Nome']}' where Id = {linguagem['Id']}")

        self.conexao.commit()

# //////////////////
# Deleta a informação do banco de dados

    def deletar_db(self, id):

        self.cursor.execute(f"Delete from Linguagens where Id = {id}")

        self.conexao.commit()