from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Setores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_setor = db.Column(db.String(80))
    def __init__(self, nome_setor):
        self.nome_setor = nome_setor

class Lojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_loja = db.Column(db.String(80))
    nome_setor = db.Column(db.String(80))
    def __init__(self, nome_loja, nome_setor):
        self.nome_loja = nome_loja
        self.nome_setor = nome_setor

class Funcionarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    tipo_funcionario = db.Column(db.String(80))
    cpf = db.Column(db.String(80))
    status = db.Column(db.String(80))
    telefone = db.Column(db.String(80))
    def __init__(self, nome_funcionario, nome_loja, tipo_funcionario, cpf, status, telefone):
        self.nome_funcionario = nome_funcionario
        self.nome_loja = nome_loja
        self.tipo_funcionario = tipo_funcionario
        self.cpf = cpf
        self.status = status
        self.telefone = telefone

class RequisicoesDeCadastros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    data_requisicao = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    def __init__(self, nome_funcionario, data_requisicao, nome_loja):
        self.nome_funcionario = nome_funcionario
        self.data_requisicao = data_requisicao
        self.nome_loja = nome_loja

class RequisicoesDePromocoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    data_requisicao = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    status = db.Column(db.String(80))
    corpo = db.Column(db.String(80))
    def __init__(self, nome_funcionario, data_requisicao, nome_loja, status, corpo):
        self.nome_funcionario = nome_funcionario
        self.data_requisicao = data_requisicao
        self.nome_loja = nome_loja
        self.status = status
        self.corpo = corpo

def insertFuncionario():
    data = Funcionarios(input('Digite o nome do funcionario: '), input('Digite o nome da loja: '), input('Digite o cargo: '), 
    input('Digite o CPF do funcionario: '), 'Ativo', input('Digite o telefone do funcionario: '))
    db.session.add(data)
    db.session.commit()

def SelectSetores():
    data_setores = Setores.query.all()
    setores = ""
    for num, d in enumerate(data_setores, start=1):
        setores += "\\n selecione " + str(num) + " para " + d
    return(setores)