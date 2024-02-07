from flask import render_template, request, redirect, url_for, flash, send_file
from app import app
import csv
import os

#Rota par ao CSV
@app.route('/dados/dados.csv')
def abrir_arquivo_csv():
    file_path = os.path.join(app.root_path, 'dados', 'dados.csv')
    return send_file(file_path, as_attachment=True)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            # Login bem-sucedido, redirecionar para a página de controle
            return redirect(url_for('controle'))
        else:
            error = 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html', error=error)

@app.route('/controle', methods=['GET', 'POST'])
def controle():
    if request.method == 'POST':
        data = request.form['data']
        hora = request.form['hora']
        pergunta = request.form['pergunta']
        
        # Arredonde o valor da velocidade para o inteiro mais próximo e converta para inteiro
        velocidade = int(round(float(request.form['velocidade'])))
        quantidade = int(request.form['quantidade'])
        resultado = quantidade / velocidade if velocidade != 0 else 0

        # Salvar os dados em um arquivo CSV
        file_path = os.path.join(app.root_path, 'dados', 'dados.csv')
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data, hora, pergunta, velocidade, quantidade, resultado])

        flash('Dados salvos com sucesso!', 'success')
        return redirect(url_for('controle'))

    return render_template('controle.html')
