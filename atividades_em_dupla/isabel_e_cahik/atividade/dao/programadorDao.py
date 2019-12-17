import MySQLdb

from model.programador import Programador

class ProgramadorDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def listar(self):
        lista_programador = []

        comando_sql_listar = """ SELECT * FROM programador """
        self.cursor.execute(comando_sql_listar)

        lista_tupla = self.cursor.fetchall()

        for l in lista_tupla:
            programador = Programador(l[1], l[0])
            lista_programador.append(programador.__dict__)
        return lista_programador

    def buscar_por_id(self, id:int):
        comando_sql_buscar_id = f""" SELECT * FROM programador WHERE id = {id} """

        self.cursor.execute(comando_sql_buscar_id)
        tupla = self.cursor.fetchone()

        programador = Programador(tupla[1], tupla[0])

        return programador.__dict__