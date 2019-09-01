from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/hackaengage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
    status = db.Column(db.String(80))
    def __init__(self, nome_funcionario, data_requisicao, status):
        self.nome_funcionario = nome_funcionario
        self.data_requisicao = data_requisicao

