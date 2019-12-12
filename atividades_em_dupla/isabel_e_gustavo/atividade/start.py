# import sys
# sys.path.append(
#     "C:/Users/900226/Desktop/exercicios/atividade_dupla/Trabalho2/")

from flask import Flask, render_template, redirect, request

from dao.listar import Listar
from dao.dao_pessoas import Pessoa_db
from dao.dao_linguagens import Linguagem_db
from dao.dao_funcionarios import Funcionario_db
from dao.dao_equipes import Equipe_db

from model.pessoas import Pessoa
from model.equipes import Equipe
from model.linguagens import Linguagem
from model.funcionarios import Funcionario


app = Flask(__name__
            # , template_folder='../templates',
            # static_folder='../static'
            )


# Rota de cadastro
@app.route('/')
def home():
    return render_template('home.html')

# Rota de listagem
@app.route('/listagem')
def listagem():
    listar = Listar()
    lista_pessoa = listar.listar_pessoas()
    lista_funcionario = listar.listar_funcionarios()
    lista_equipe = listar.listar_equipes()
    lista_linguagem = listar.listar_linguagens()
    return render_template('listagem.html', pessoa=lista_pessoa, funcionario=lista_funcionario, equipe=lista_equipe, linguagem=lista_linguagem)

# Rota que cadastra a pessoa
@app.route('/salvar_pessoa')
def salvar_pessoa():
    pessoa = Pessoa_db()
    nome = request.args["nome"]
    cpf = request.args["cpf"]
    telefone = request.args["telefone"]
    pessoa.set_cadastrar(nome, cpf, telefone)
    pessoa.cadastrar_db(pessoa.get_cadastrar())
    return redirect('/listagem')

# Rota que cadastra o funcionário
@app.route('/salvar_funcionario')
def salvar_funcionario():
    funcionario = Funcionario_db()
    idpessoal = request.args["id-pessoal"]
    cargo = request.args["cargo"]
    salario = request.args["salario"]
    funcionario.set_cadastrar(cargo, salario, idpessoal)
    funcionario.cadastrar_db(funcionario.get_cadastrar())
    return redirect('/listagem')

# Rota que cadastra a linguagem
@app.route('/salvar_linguagem')
def salvar_linguagem():
    linguagem = Linguagem_db()
    nome = request.args["linguagem"]
    linguagem.set_cadastrar(nome)
    linguagem.cadastrar_db(linguagem.get_cadastrar())
    return redirect('/listagem')

# Rota que cadastra a equipe
@app.route('/salvar_equipe')
def salvar_equipe():
    equipe = Equipe_db()
    funcionario1 = request.args["funcionario1"]
    funcionario2 = request.args["funcionario2"]
    funcionario3 = request.args["funcionario3"]
    funcionario4 = request.args["funcionario4"]
    equipe.set_cadastrar(funcionario1, funcionario2,
                         funcionario3, funcionario4)
    equipe.cadastrar_db(equipe.get_cadastrar())
    return redirect('/listagem')

# Rota de edição (individual)
@app.route('/editar')
def editar():

    retornar = Listar()

    if 'id_pessoal' in request.args.keys():
        lista = retornar.funcionario_individual(request.args['id_pessoal'])
    elif 'id_equipe' in request.args.keys():
        lista = retornar.equipe_individual(request.args['id_equipe'])
    elif 'id_linguagem' in request.args.keys():
        lista = retornar.linguagem_individual(request.args['id_linguagem'])

    return render_template('editar.html', pessoa=lista)

# Rota que edita ou deleta um funcionario e a pessoa
@app.route('/editar_funcionario', methods=['POST'])
def editar_funcionario():
    func = Funcionario_db()
    pess = Pessoa_db()
    if 'deletar' in request.form.keys():
        func.deletar_db(request.form['id_funcionario'])
        pess.deletar_db(request.form['id_pessoal'])
    elif 'alterar' in request.form.keys():
        func.set_editar(request.form['id_funcionario'],
                        request.form['cargo'], request.form['salario'])
        func.editar_db(func.get_editar())
        pess.set_editar(request.form['id_pessoal'], request.form['nome'],
                        request.form['cpf'], request.form['telefone'])
        pess.editar_db(pess.get_editar())

    return redirect('/listagem')

# Rota que edita ou deleta a linguagem
@app.route('/editar_linguagem', methods=['POST'])
def editar_linguagem():
    lg = Linguagem_db()
    if 'deletar' in request.form.keys():
        lg.deletar_db(request.form['id_linguagem'])
    elif 'alterar' in request.form.keys():
        lg.set_editar(request.form['id_linguagem'],
                      request.form['nome'])
        lg.editar_db(lg.get_editar())

    return redirect('/listagem')

# Rota que edita ou deleta a equipe
@app.route('/editar_equipe', methods=['POST'])
def editar_equipe():
    eq = Equipe_db()
    if 'deletar' in request.form.keys():
        eq.deletar_db(request.form['id_equipe'])
    elif 'alterar' in request.form.keys():
        eq.set_editar(request.form['id_equipe'],
                        request.form['id1'], request.form['id2'], request.form['id3'], request.form['id4'])
        eq.editar_db(eq.get_editar())

    return redirect('/listagem')


app.run(debug=True)
