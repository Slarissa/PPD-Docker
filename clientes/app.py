from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="controle_vendas"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return jsonify(clientes)
    except mysql.connector.Error as err:
        return jsonify({"message": f"Erro ao listar clientes: {err}"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    data = request.json
    
    if not data or "nome" not in data or "telefone" not in data or not data["nome"].strip() or not data["telefone"].strip():
        return jsonify({"message": "Dados inválidos. Nome e telefone são obrigatórios."}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (data["nome"], data["telefone"]))
        conn.commit()
        
        if cursor.rowcount > 0:
            return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201
        else:
            return jsonify({"message": "Erro ao cadastrar cliente."}), 500
    except mysql.connector.Error as err:
        return jsonify({"message": f"Erro ao cadastrar cliente: {err}"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
