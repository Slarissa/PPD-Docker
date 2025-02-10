from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="vendas"
    )

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    conn = db_connection()
    cursor = conn.cursor()

    nome = request.json['nome']
    descricao = request.json['descricao']
    valor = request.json['valor']

    cursor.execute("INSERT INTO produtos (nome, descricao, valor) VALUES (%s, %s, %s)",
                   (nome, descricao, valor))
    conn.commit()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
