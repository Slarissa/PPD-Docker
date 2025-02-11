CREATE DATABASE IF NOT EXISTS controle_vendas;

USE controle_vendas;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(10, 2) NOT NULL
);

INSERT INTO produtos (nome, descricao, valor) VALUES
('Produto 1', 'Descrição do Produto 1', 19.99),
('Produto 2', 'Descrição do Produto 2', 29.99),
('Produto 3', 'Descrição do Produto 3', 39.99);
