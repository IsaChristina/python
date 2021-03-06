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

    def buscar_por_id(self, id:int):
        comando_sql_buscar_id = f""" SELECT * FROM framework WHERE id_framework = {id} """
        
        self.cursor.execute(comando_sql_buscar_id)
        tupla = self.cursor.fetchone()
        
        framework = Framework(tupla[1], tupla[0])

        return framework.__dict__