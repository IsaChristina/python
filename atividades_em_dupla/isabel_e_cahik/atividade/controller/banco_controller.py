from flask_restful import Resource

from dao.bancoDao import BancoDao

class BancoController(Resource):

    def __init__(self):
        self.dao = BancoDao()

    def get(self):
        return self.dao.listar()