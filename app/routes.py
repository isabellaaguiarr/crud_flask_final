from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Dados

@app.route('/')
def index():
    items_ = Dados.query.all()
    return render_template('index.html', items=items_)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome_livro  = request.form['nome_livro']
        autor = request.form['autor']
        genero_textual = request.form['genero_textual']
        avaliacao = request.form['avaliacao']
        new_item = Dados(nome_livro=nome_livro, autor=autor, genero_textual=genero_textual , avaliacao=avaliacao )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Dados.query.get_or_404(id)
    if request.method == 'POST':
        item.nome_livro = request.form['nome_livro']
        item.autor = request.form['autor']
        item.genero_textual = request.form['genero_textual']
        item.avaliacao = request.form['avaliacao']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Dados.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))


