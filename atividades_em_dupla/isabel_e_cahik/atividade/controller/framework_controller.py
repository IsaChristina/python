from flask_restful import Resource

from dao.frameworkDao import FrameworkDao

class FrameworkController(Resource):

    def __init__(self):
        self.dao = FrameworkDao()

    def get(self, id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()