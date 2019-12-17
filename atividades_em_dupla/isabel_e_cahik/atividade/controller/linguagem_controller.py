from flask_restful import Resource

from dao.linguagemDao import LinguagemDao

class LinguagemController(Resource):

    def __init__(self):
        self.dao = LinguagemDao()

    def get(self, id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()