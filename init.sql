CREATE DATABASE IF NOT EXISTS controle_vendas;

USE controle_vendas;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(10, 2) NOT NULL
);

INSERT INTO produtos (nome, descricao, valor) VALUES
('Produto 1', 'Detalhes do Produto 1', 19.99),
('Produto 2', 'Detalhes do Produto 2', 29.99),
('Produto 3', 'Detalhes do Produto 3', 39.99);


CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

INSERT INTO clientes (nome, telefone) VALUES
('Ana Silva', '41111111111'),
('Maria Souza', '4222222222'),
('Carlos Lima', '43333333333');


CREATE TABLE IF NOT EXISTS vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    cliente_id INT,
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor DECIMAL(10, 2),
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);