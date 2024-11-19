from app import db 
class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_livro = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero_textual = db.Column(db.String(100), nullable=False)
    avaliacao = db.Column(db.String(100), nullable=False)