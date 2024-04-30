CREATE TABLE UNIDADE_PRODUCAO (
    numero int PRIMARY KEY,
    peca_hora_nominal real
);

CREATE TABLE REGISTRO_FALHA (
    id int PRIMARY KEY,
    severidade BIT,
    inicio datetime,
    fim datetime,
    numero_unidade_producao int,
    FOREIGN KEY (numero_unidade_producao) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE PECA(
    numero int PRIMARY KEY,
    status varchar(10) CHECK (status IN ('Aprovada', 'Reprovada')),
    inicio_fabricacao datetime,
    fim_fabricacao datetime,
    numero_unidade_producao int,
    FOREIGN KEY (numero_unidade_producao) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE SOPRADORA(
    numero int PRIMARY KEY,
    vazao_sopro real,
    pressao_sopro real,
    FOREIGN KEY (numero) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE FRESADORA(
    numero int PRIMARY KEY,
    velocidade_rotacao real,
    profundidade_corte real,
    FOREIGN KEY (numero) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE TORNO_CNC(
    numero int PRIMARY KEY,
    velocidade_rotacao real,
    tolerancia real,
    FOREIGN KEY (numero) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IMPRESSORA_3D(
    numero int PRIMARY KEY,
    espessura_camada real,
    tipo_material varchar (30),
    FOREIGN KEY (numero) 
        REFERENCES UNIDADE_PRODUCAO(numero)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
