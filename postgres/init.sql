CREATE TABLE cadastro (
    cad_usuario VARCHAR(50) PRIMARY KEY,
    nome VARCHAR(50),
    apelido VARCHAR(10),
    email VARCHAR(30),
    celular VARCHAR(15),
    renda FLOAT
);

CREATE TABLE _login (
    usuario VARCHAR(50) PRIMARY KEY,
    senha VARCHAR(50) NOT NULL
    FOREIGN KEY (usuario) REFERENCES cadastro (cad_usuario)
);

CREATE TABLE gastos (
    gt_usuario VARCHAR(50) PRIMARY KEY,
    produto VARCHAR(10),
    valor FLOAT,
    estabelecimento VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    FOREIGN KEY (gt_usuario) REFERENCES cadastro (cad_usuario)
);

CREATE TABLE rankings (
    rn_usuario VARCHAR(50),
    percentual FLOAT,
    FOREIGN KEY (rn_usuario) REFERENCES cadastro (cad_usuario)
);

CREATE TABLE clientes (
    cl_apelido VARCHAR(50) PRIMARY KEY,
    cl_usuario VARCHAR(15),
    FOREIGN KEY (cl_usuario) REFERENCES cadastro (cad_usuario)
);