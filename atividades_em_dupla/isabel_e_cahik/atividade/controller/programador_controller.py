from flask_restful import Resource

from dao.programadorDao import ProgramadorDao

class ProgramadorController(Resource):

    def __init__(self):
        self.dao = ProgramadorDao()

    def get(self):
        return self.dao.listar()