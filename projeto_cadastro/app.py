from flask import Flask, render_template, request, jsonify
import re
import mysql.connector

app = Flask(__name__)

# Configuração de conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",       # Onde está seu MySQL (se for local, é localhost)
    user="root",            # Seu usuário do MySQL
    password="Minhasenha01*",   # Sua senha do MySQL
    database="cadastro_usuarios"  # Nome do banco
)

def validar_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def validar_senha(senha):
    return re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', senha)

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')
    confirmar_senha = dados.get('confirmar_senha')

    if not validar_email(email):
        return jsonify({'status': 'erro', 'mensagem': 'E-mail inválido!'})

    if not validar_senha(senha):
        return jsonify({'status': 'erro', 'mensagem': 'Senha fraca! Mínimo 8 caracteres, 1 maiúscula, 1 número e 1 caractere especial.'})

    if senha != confirmar_senha:
        return jsonify({'status': 'erro', 'mensagem': 'As senhas não coincidem!'})

    # Inserindo no banco
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (email, senha) VALUES (%s, %s)"
        valores = (email, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        return jsonify({'status': 'sucesso', 'mensagem': 'Cadastro realizado com sucesso!'})
    except mysql.connector.Error as err:
        print(err)
        return jsonify({'status': 'erro', 'mensagem': 'Erro ao salvar no banco de dados! Verifique se o e-mail já foi cadastrado.'})

if __name__ == '__main__':
    app.run(debug=True)
