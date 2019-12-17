import MySQLdb

from model.banco import Banco

class BancoDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def listar(self):
        lista_banco = []

        comando_sql_listar = """ SELECT * FROM banco """
        self.cursor.execute(comando_sql_listar)

        lista_tupla = self.cursor.fetchall()

        for l in lista_tupla:
            banco = Banco(l[1], l[0])
            lista_banco.append(banco.__dict__)
        return lista_banco