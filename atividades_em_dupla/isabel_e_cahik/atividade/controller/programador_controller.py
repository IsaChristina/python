from flask_restful import Resource

from dao.programadorDao import ProgramadorDao

class ProgramadorController(Resource):

    def __init__(self):
        self.dao = ProgramadorDao()

    def get(self, id:int):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()