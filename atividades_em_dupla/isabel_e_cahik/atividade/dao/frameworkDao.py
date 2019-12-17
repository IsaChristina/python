import MySQLdb

from model.framework import Framework

class FrameworkDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def listar(self):
        lista_framework = []

        comando_sql_listar = """ SELECT * FROM framework """
        self.cursor.execute(comando_sql_listar)

        lista_tupla = self.cursor.fetchall()

        for l in lista_tupla:
            framework = Framework(l[1], l[0])
            lista_framework.append(framework.__dict__)
        return lista_framework