from flask_restful import Resource

from dao.squadDao import SquadDao

class SquadController(Resource):

    def __init__(self):
        self.dao = SquadDao()

    def get(self, id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()