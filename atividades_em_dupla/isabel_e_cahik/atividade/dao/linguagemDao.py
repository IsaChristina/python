import MySQLdb

from model.linguagem import Linguagem

class LinguagemDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def listar(self):
        lista_linguagem = []

        comando_sql_listar = """ SELECT * FROM linguagem """
        self.cursor.execute(comando_sql_listar)

        lista_tupla = self.cursor.fetchall()

        for l in lista_tupla:
            linguagem = Linguagem(l[1], l[0])
            lista_linguagem.append(linguagem.__dict__)
        return lista_linguagem

    def buscar_por_id(self, id:int):
        comando_sql_buscar_id = f""" SELECT * FROM linguagem WHERE id_linguagem = {id} """
        
        self.cursor.execute(comando_sql_buscar_id)
        tupla = self.cursor.fetchone()
        
        linguagem = Linguagem(tupla[1], tupla[0])

        return linguagem.__dict__
