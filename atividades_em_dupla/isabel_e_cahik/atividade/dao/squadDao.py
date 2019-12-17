import MySQLdb

from model.squad import Squad

from model.banco import Banco

from model.framework import Framework

from model.linguagem import Linguagem

from model.programador import Programador


class SquadDao:

    def __init__(self):
        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def listar(self):
        lista_squad = []
        comando_sql_listar = """ SELECT  b.id_banco,
                                    b.nome_banco,
                                    l.id_linguagem,
                                    l.nome_linguagem,
                                    f.id_framework,
                                    f.nome_framework,
                                    p.id,
                                    p.nome 
                                    FROM squad as s
                                    JOIN banco as b
                                    ON s.id_banco = b.id_banco
                                    JOIN linguagem as l
                                    ON s.id_linguagem = l.id_linguagem
                                    JOIN framework as f
                                    ON s.id_framework = f.id_framework
                                    JOIN programador as p
                                    ON s.id_programador = p.id """
        # lista_tupla = super().listar(comando_sql_listar)
        self.cursor.execute(comando_sql_listar)
        lista_tupla = self.cursor.fetchall()
        for l in lista_tupla:
            banco = Banco(l[1], l[0])
            linguagem = Linguagem(l[3], l[2])
            framework = Framework(l[5], l[4])
            programador = Programador(l[7], l[6])
            squad = Squad(programador.__dict__, linguagem.__dict__, framework.__dict__, banco.__dict__)
            lista_squad.append(squad.__dict__)
        return lista_squad
    
    def buscar_por_id(self, id:int):
        comando_sql_buscar_id = f""" SELECT  b.id_banco,
                                        b.nome_banco,
                                        l.id_linguagem,
                                        l.nome_linguagem,
                                        f.id_framework,
                                        f.nome_framework,
                                        p.id,
                                        p.nome 
                                        FROM squad as s
                                        JOIN banco as b
                                        ON s.id_banco = b.id_banco
                                        JOIN linguagem as l
                                        ON s.id_linguagem = l.id_linguagem
                                        JOIN framework as f
                                        ON s.id_framework = f.id_framework
                                        JOIN programador as p
                                        ON s.id_programador = p.id
                                        WHERE s.id_programador = {id}"""
        self.cursor.execute(comando_sql_buscar_id)
        tupla = self.cursor.fetchone()
        banco = Banco(tupla[1], tupla[0])
        linguagem = Linguagem(tupla[3], tupla[2])
        framework = Framework(tupla[5], tupla[4])
        programador = Programador(tupla[7], tupla[6])
        squad = Squad(programador.__dict__, linguagem.__dict__, framework.__dict__, banco.__dict__)
        return squad.__dict__