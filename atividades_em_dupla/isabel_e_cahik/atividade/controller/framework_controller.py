from flask_restful import Resource

from dao.frameworkDao import FrameworkDao

class FrameworkController(Resource):

    def __init__(self):
        self.dao = FrameworkDao()

    def get(self):
        return self.dao.listar()