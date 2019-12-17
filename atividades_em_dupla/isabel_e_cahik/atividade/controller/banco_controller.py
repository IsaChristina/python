from flask_restful import Resource

from dao.bancoDao import BancoDao

class BancoController(Resource):

    def __init__(self):
        self.dao = BancoDao()

    def get(self, id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()