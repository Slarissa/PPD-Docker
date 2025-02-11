const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());

const mysql = require('mysql2');

const db = mysql.createConnection({
    host: 'mysql', 
    user: 'root',
    password: 'root',
    database: 'controle_vendas'
});

db.connect(err => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err);
        return;
    }
    console.log('Conectado ao banco de dados!');
});

app.post('/vendas', (req, res) => {
    const { clienteId, produtoId, valor } = req.body;

    if (!clienteId || !produtoId || !valor) {
        return res.status(400).json({ error: 'Todos os campos são obrigatórios!' });
    }

    const query = 'INSERT INTO vendas (cliente_id, produto_id, valor) VALUES (?, ?, ?)';

    db.execute(query, [clienteId, produtoId, valor], (err, results) => {
        if (err) {
            console.error('Erro ao salvar a venda:', err);
            return res.status(500).json({ error: 'Erro ao salvar a venda!' });
        }

        res.status(201).json({
            message: 'Venda realizada com sucesso!',
            venda: {
                id: results.insertId,  
                clienteId,
                produtoId,
                valor,
                data: new Date()
            }
        });
    });
});

app.get('/vendas', (req, res) => {
    const query = 'SELECT * FROM vendas';

    db.execute(query, (err, results) => {
        if (err) {
            console.error('Erro ao listar as vendas:', err);
            return res.status(500).json({ error: 'Erro ao listar as vendas!' });
        }

        res.status(200).json(results);
    });
});

const PORT = process.env.PORT || 5003;
app.listen(PORT, () => {
    console.log(`Servidor de vendas rodando na porta ${PORT}`);
});
