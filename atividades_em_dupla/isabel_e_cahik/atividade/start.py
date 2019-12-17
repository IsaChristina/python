from flask import Flask
from flask_restful import Api
from controller.banco_controller import BancoController
from controller.framework_controller import FrameworkController
from controller.linguagem_controller import LinguagemController
from controller.programador_controller import ProgramadorController
from controller.squad_controller import SquadController

app = Flask(__name__)

api = Api(app)

api.add_resource(BancoController, '/api/banco')
api.add_resource(BancoController, '/api/banco/<int:id>', endpoint = 'banco')

api.add_resource(FrameworkController, '/api/framework')
api.add_resource(FrameworkController, '/api/framework/<int:id>', endpoint = 'framework')

api.add_resource(LinguagemController, '/api/linguagem')
api.add_resource(LinguagemController, '/api/linguagem/<int:id>', endpoint = 'linguagem')

api.add_resource(ProgramadorController, '/api/programador')
api.add_resource(ProgramadorController, '/api/programador/<int:id>', endpoint = 'programador')

api.add_resource(SquadController, '/api/squad')
api.add_resource(SquadController, '/api/squad/<int:id>', endpoint = 'squad')

app.run(debug=True)