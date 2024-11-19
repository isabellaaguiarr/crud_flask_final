import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meu_novo_banco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave'
