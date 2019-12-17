from model.banco import Banco
from model.framework import Framework
from model.linguagem import Linguagem
from model.programador import Programador

class Squad:
    def __init__(self, programador:Programador, linguagem:Linguagem, framework:Framework, banco:Banco):
        self.programador = programador
        self.linguagem = linguagem
        self.framework = framework
        self.banco = banco
