<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

$host = 'mysql';
$dbname = 'controle_vendas';
$username = 'root';
$password = 'root';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


    header('Content-Type: application/json');

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $data = json_decode(file_get_contents('php://input'), true);

        if (isset($data['nome'], $data['descricao'], $data['valor'])) {
            $stmt = $pdo->prepare("INSERT INTO produtos (nome, descricao, valor) VALUES (:nome, :descricao, :valor)");
            $stmt->bindParam(':nome', $data['nome']);
            $stmt->bindParam(':descricao', $data['descricao']);
            $stmt->bindParam(':valor', $data['valor'], PDO::PARAM_STR);

            if ($stmt->execute()) {
                echo json_encode(['message' => 'Produto cadastrado com sucesso!']);
            } else {
                echo json_encode(['message' => 'Erro ao cadastrar produto.']);
            }
        } else {
            echo json_encode(['message' => 'Dados inválidos ou incompletos']);
        }
    } else {
        $stmt = $pdo->query("SELECT * FROM produtos");
        $produtos = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($produtos);
    }
} catch (PDOException $e) {
    echo json_encode(['message' => 'Erro ao conectar ao banco de dados: ' . $e->getMessage()]);
}
