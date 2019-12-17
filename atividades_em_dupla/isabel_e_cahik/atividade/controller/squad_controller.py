import MySQLdb
from flask_restful import Resource
from flask import request

from dao.squadDao import SquadDao
from model.squad import Squad

class SquadController(Resource):

    def __init__(self):
        self.dao = SquadDao()

        self.conexao = MySQLdb.connect(host = "mysql.topskills.study",
                                        database = "topskills12",
                                        user = "topskills12",
                                        passwd = "Isabel2019")
        self.cursor = self.conexao.cursor()

    def get(self, id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()

    def post(self):
        # comando_sql_count = """ SELECT COUNT(id_programador) FROM squad """
        # count = self.cursor.execute(comando_sql_count)

        # lista_dados = []

        programador_id = request.json["programador_id"]
        linguagem_id = request.json["linguagem_id"]
        framework_id = request.json["framework_id"]
        banco_id = request.json["banco_id"]

        squad = Squad(programador_id, linguagem_id, framework_id, banco_id)
        squad_id = self.dao.inserir(squad)
        # lista_dados.append(programador_id)
        # lista_dados.append(linguagem_id)
        # lista_dados.append(framework_id)
        # lista_dados.append(banco_id)
        return squad_id
        

        # fazer verificação se tem 3 inseridos
        # fazer verificação se podem ser inseridos
        # fazer método inserir em todas as classes
