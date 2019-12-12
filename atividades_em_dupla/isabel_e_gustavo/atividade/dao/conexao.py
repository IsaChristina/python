import MySQLdb

#  Inicia a classe de conexão
class Conexao:

    def __init__(self):
        
        self.conexao = MySQLdb.connect(host='mysql.topskills.study',
                                       database='topskills11', user='topskills11', passwd='Gustavo2019')
        self.cursor = self.conexao.cursor()
