CREATE SCHEMA FARMACIA AUTHORIZATION postgres;

SET search_path TO farmacia, public;
SET datestyle TO ISO, DMY;

CREATE TABLE CLIENTE (
CPF CHAR(11)   NOT NULL,
	NOME   VARCHAR(30)   NOT NULL,
	DATA_NASCIMENTO   DATE,
EMAIL  VARCHAR(30),
	ENDERECO   VARCHAR(50),
	SEXO   CHAR(1),
	ID_BENEFICIOS   CHAR(2),

	PRIMARY KEY (CPF)
);

CREATE TABLE CLIENTE_TELEFONES (
CPF CHAR(11)   NOT NULL,
	TELEFONE  CHAR(11)   NOT NULL,

	PRIMARY KEY (CPF, TELEFONE),
	FOREIGN KEY (CPF) REFERENCES CLIENTE (CPF)
);

CREATE TABLE PROGRAMA_BENEFICIOS (
ID CHAR(2)   NOT NULL,
	NOME   VARCHAR(50)   NOT NULL,
	DESCRICAO VARCHAR(200),
FATOR_DESCONTO CHAR(2)   NOT NULL,

	PRIMARY KEY (ID),
	UNIQUE (NOME)
);
ALTER TABLE CLIENTE ADD CONSTRAINT FK_BENEFICIOS FOREIGN KEY (ID_BENEFICIOS) REFERENCES PROGRAMA_BENEFICIOS (ID);
CREATE TABLE FUNCIONARIO (
FUNCIONAL CHAR(7)   NOT NULL,
	NOME   VARCHAR(30)   NOT NULL,
DATA_NASCIMENTO   DATE,
ENDERECO   VARCHAR(50),
SALARIO   DECIMAL(10,2) NOT NULL,
	SEXO   CHAR(1),
	TIPO_FUNC VARCHAR(50) NOT NULL,
	CRF CHAR(6),

	PRIMARY KEY (FUNCIONAL),
	UNIQUE (CRF)
);

CREATE TABLE FUNCIONARIO_TELEFONES (
FUNCIONAL CHAR(7)   NOT NULL,
	TELEFONE  CHAR(11)   NOT NULL,
	
	PRIMARY KEY (FUNCIONAL, TELEFONE),
	FOREIGN KEY (FUNCIONAL) REFERENCES FUNCIONARIO (FUNCIONAL)
);

CREATE TABLE TURNO (
FUNCIONAL CHAR(7)   NOT NULL,
	DATA_HORA_ENTRADA   DATE   NOT NULL,
	DATA_HORA_SAIDA   DATE   NOT NULL,
	DESCRICAO   VARCHAR(200),

	PRIMARY KEY (FUNCIONAL, DATA_HORA_ENTRADA),
	FOREIGN KEY (FUNCIONAL) REFERENCES FUNCIONARIO (FUNCIONAL)
);

CREATE TABLE SERVICO (
ID CHAR(10)   NOT NULL,
	PRECO  DECIMAL(10,2)   NOT NULL,
	DESCRICAO VARCHAR(200),
NOME VARCHAR(50)   NOT NULL,

	PRIMARY KEY (ID),
	UNIQUE (NOME)
);

CREATE TABLE SERVICO_REALIZADO (
CODIGO CHAR(10)   NOT NULL,
	ID_SERVICO  CHAR(10)   NOT NULL,
	CPF_CLIENTE   CHAR(11)   NOT NULL,
NUM_FUNC   CHAR(7)   NOT NULL,
DATA DATE,

	PRIMARY KEY (CODIGO),
	FOREIGN KEY (ID_SERVICO) REFERENCES SERVICO (ID),
FOREIGN KEY (CPF_CLIENTE) REFERENCES CLIENTE (CPF),
FOREIGN KEY (NUM_FUNC) REFERENCES FUNCIONARIO (FUNCIONAL)
);

CREATE TABLE COMPRA (
CPF_CLIENTE   CHAR(11),
	CODIGO_COMPRA   CHAR(9)   NOT NULL,
	NUM_FUNC   CHAR(7)   NOT NULL,
	TOTAL   DECIMAL(10,2)   NOT NULL,
	DATA DATE,
FORMA_PAGAMENTO   VARCHAR(16)   NOT NULL,
DESCONTO   DECIMAL(10,2),

	PRIMARY KEY (CODIGO_COMPRA),
FOREIGN KEY (CPF_CLIENTE) REFERENCES CLIENTE (CPF),
	FOREIGN KEY (NUM_FUNC) REFERENCES FUNCIONARIO (FUNCIONAL)
);

CREATE TABLE COMPRA_PRODUTO (
CODIGO_COMPRA   CHAR(9)   NOT NULL,
	CODIGO_BARRAS  CHAR(12)   NOT NULL,
	QUANTIDADE INT,

	PRIMARY KEY (CODIGO_COMPRA, CODIGO_BARRAS),
	FOREIGN KEY (CODIGO_COMPRA) REFERENCES COMPRA(CODIGO_COMPRA )
);

CREATE TABLE PRODUTO (
CODIGO_BARRAS  CHAR(12)   NOT NULL,
	NOME  VARCHAR(50)   NOT NULL,
	CATEGORIA  VARCHAR(15)   NOT NULL,
	PRECO  DECIMAL(10,2)   NOT NULL,

	PRIMARY KEY (CODIGO_BARRAS),
UNIQUE (NOME)
);

ALTER TABLE COMPRA_PRODUTO ADD CONSTRAINT FK_COD_BARRAS FOREIGN KEY (CODIGO_BARRAS) REFERENCES PRODUTO (CODIGO_BARRAS);
CREATE TABLE FORNECEDOR (
CNPJ CHAR(14)   NOT NULL,
	EMAIL   VARCHAR(30),
	ENDERECO   VARCHAR(50),
	RAZAO_SOCIAL   VARCHAR(30),

	PRIMARY KEY (CNPJ),
	UNIQUE (RAZAO_SOCIAL)

);

CREATE TABLE FORNECEDOR_TELEFONES (
CNPJ_FORN CHAR(14)   NOT NULL,
	TELEFONE   CHAR(11) NOT NULL,

	PRIMARY KEY (CNPJ_FORN, TELEFONE),
	FOREIGN KEY (CNPJ_FORN) REFERENCES FORNECEDOR (CNPJ)
);

CREATE TABLE SOLICITACAO_PRODUTO (
NUM_FUNC   CHAR(7)   NOT NULL,
NUMERO_PEDIDO   VARCHAR(10)   NOT NULL,
CODIGO_BARRAS  CHAR(12)   NOT NULL,
CNPJ_FORN CHAR(14)   NOT NULL,
QUANTIDADE   INT,
DATA_DE_VALIDADE   DATE,
DATA_SOLICITACAO   DATE,
VALOR_TOTAL   DECIMAL(10,2) NOT NULL,


	PRIMARY KEY (NUMERO_PEDIDO),
FOREIGN KEY (NUM_FUNC) REFERENCES FUNCIONARIO (FUNCIONAL),
FOREIGN KEY (CODIGO_BARRAS) REFERENCES PRODUTO (CODIGO_BARRAS),
	FOREIGN KEY (CNPJ_FORN) REFERENCES FORNECEDOR (CNPJ)
	
);

 INSERT INTO programa_beneficios(ID, Nome, Descricao, Fator_Desconto) VALUES
('1', 'Desconto Fidelidade', 'Desconto para clientes que compram frenquentemente', '25'),
('2', 'Queima Estoque Higiene', 'Queima de estoque para produtos de higiene', '30'),
('3', 'Leve dois e pague um', 'Na compra de 2 remédios, pague apenas 1', '50'),
('4', 'Black Friday', 'Descontos em produtos diversos', '20'),
('5', 'Remédios Populares', 'Subsidio na compra de remédios cadastrados pelo Farmacia Popular', '90');

INSERT INTO cliente(cpf, nome, data_nascimento, email, endereco, sexo, id_beneficios) VALUES
('68043875030', 'Jose Maria Silva', '25-10-1995', 'josemaria@email.com.br', 'Rua Brasil, 100', 'M', 1),
('63191822020', 'Maria Jose Silva', '25-10-1996', 'mariajose@email.com.br', 'Rua EUA, 101', 'F', 2),
('00559460031', 'Adailton Melo', '25-04-1997', 'dailtomelo@email.com.br', 'Rua Venezuela, 102', 'M', 3),
('96669265042', 'Marta Abreu', '12-06-1998', 'martinhabreu@email.com.br', 'Rua Cuba, 13', 'F', 4),
('70742547035', 'James Igor', '23-07-1999', 'jigor@email.com.br', 'Rua Portugal, 200', 'M', 5),
('39531904073', 'Anna Carolina Texeira', '11-11-2000', 'carolat@email.com.br', 'Rua França, 82', 'F', 1),
('11980749060', 'Timoteo Souza', '12-04-2001', 'souzatimoteo@email.com.br', 'Rua Russia, 104', 'M', 1),
('76068362051', 'Antonia Tabata de Lima', '13-02-2002', 'antonitabatalima@email.com.br', 'Rua Italia, 21', 'F', 2),
('29304490049', 'Gabriel Lima', '05-03-1994', 'gabriellima@email.com.br', 'Rua Belgica, 15', 'M', 2),
('19558162043', 'Gustavo da Conceição', '01-01-1993', 'conceicagusta@email.com.br', 'Rua Egito, 14', 'M', 3),
('71042853002', 'Helena Santos Matoso', '21-09-1992', 'helenamatoso@email.com.br', 'Rua China, 13', 'F', 3),
('52781063010', 'Joyce Gasques Silveira', '30-05-1995', 'jsilveiragasq@email.com.br', 'Rua Taiwan, 12', 'F', 4),
('25879781062', 'Joao Campos Matos', '28-10-1991', 'joaocampos@email.com.br', 'Rua Chile, 11', 'M', 4),
('59931225017', 'Marcela Marques', '21-12-1990', 'mmarcelamarques@email.com.br', 'Rua Argentina, 10', 'F', 5),
('43254364352', 'Eduardo Ferreira', '21-08-1992', 'eduardoferreira@email.com.br', 'Rua México, 41', 'M', 1),
('65424321433', 'Anna Alice Soares', '06-08-1985', 'analicesoares@email.com.br', 'Rua Canada, 22', 'F', 1),
('32543635432', 'Diogo Cruz', '01-12-1968', 'diogocruz@email.com.br', 'Rua Colombia, 10', 'M', 2),
('56563342147', 'Daniela Santos', '21-12-1979', 'danielasantos@email.com.br', 'Rua Japão, 82', 'F', 3),
('32424521467', 'Abner Rodrigues', '15-01-1981', 'abnerrodrigues@email.com.br', 'Rua Argentina, 48', 'M', 4),
('59234125017', 'Márcia Conceição', '11-02-1987', 'marciaconceicao@email.com.br', 'Rua Malásia, 34', 'F', 5);

INSERT INTO cliente_telefones(cpf, telefone) VALUES
('68043875030', '11965476233'),
('63191822020', '11990483790'),
('00559460031', '11987234590'),
('96669265042', '11912358793'),
('70742547035', '11976564891'),
('39531904073', '11953536862'),
('11980749060', '11965784783'),
('76068362051', '11932459092'),
('29304490049', '11909029421'),
('19558162043', '11954849302'),
('71042853002', '11992345432'),
('52781063010', '11913344533'),
('25879781062', '11923455566'),
('59931225017', '11919192345'),
('43254364352', '11932478324'),
('65424321433', '11987432743'),
('32543635432', '11988923831'),
('56563342147', '11932183128'),
('32424521467', '11921381282'),
('59234125017', '11932189315');

 INSERT INTO funcionario(funcional, nome, data_nascimento, endereco, salario, sexo, tipo_func, crf) VALUES
('9873260', 'Glauco Costa', '15-09-1987', 'Rua das Arvores, 102', 3450.73, 'M', 'farmaceutico', 321345),
('9873261', 'Glauce Silva', '21-11-1970', 'Rua das Ameixas, 1012', 5215.00, 'F', 'farmaceutico', 321478),
('9873262', 'Giovanna Souza Cruz', '27-03-2003', 'Rua das Andorinhas, 44', 1200.21, 'F', 'farmaceutico', 321987),
('9873263', 'Marco Antonio Dias', '30-10-1995', 'Rua das Parreiras, 1000', 2000.00, 'M', 'farmaceutico', 123876),
('9873264', 'Giovanni Arruda', '15-05-1981', 'Rua das Pétalas, 52', 1500.00, 'M', 'farmaceutico', 189769),
('9873265', 'Michele Aparecida', '24-12-2000', 'Rua do Café, 120', 990.12, 'F', 'atendente', NULL),
('9873266', 'Jacira do Carmo', '05-11-1990', 'Rua das Marés, 01A', 3450.73, 'F', 'atendente', NULL),
('9873267', 'Jair Bento', '15-09-1968', 'Rua da Amendoeira, 109', 6000.00, 'M', 'atendente', NULL),
('9873268', 'Marcelo Queiroz', '25-07-1970', 'Rua dos Passaros, 04', 6000.00, 'M', 'atendente', NULL),
('9873269', 'Fernanda Dias', '02-09-1981', 'Rua das maçãs, 1004', 4234.55, 'F', 'atendente', NULL),
('9873270', 'Adriano Dias', '10-04-1998', 'Rua das freiras, 205', 1500.43, 'M', 'atendente', NULL),
('9873271', 'Victoria Gonçalves', '10-10-2003', 'Rua das marés, 10', 990.12, 'F', 'gerente', NULL),
('9873272', 'Victor Ferraz', '10-04-1992', 'Rua das emoções, 25', 4234.55, 'M', 'gerente', NULL),
('9873273', 'Monica Matos', '07-10-1980', 'Rua do Café, 100', 3450.73, 'F', 'faxineiro', NULL),
('9873274', 'Erick Fernandez', '10-04-1990', 'Rua das ameixas, 12', 2000.00, 'M', 'faxineiro', NULL),
('9873275', 'Deniel Rosa', '22-09-1985', 'Rua das estrelas, 91', 4234.55, 'F', 'vigia', NULL),
('9873276', 'Marcos Silveira', '25-05-1998', 'Rua das estrelas, 44', 990.12, 'M', 'vigia', NULL),
('9873277', 'Livia Abreu', '25-04-1989', 'Rua dos Lírios, 32', 5215.00, 'F', 'vigia', NULL),
('9873278', 'Marcio Silva', '06-02-1981', 'Rua dos Lírios, 01b', 6000.00, 'M', 'administrativo', NULL),
('9873279', 'Ester Lopes', '10-01-2001', 'Rua das canelas, 103', 1200.21, 'F', 'administrativo', NULL);

INSERT INTO funcionario_telefones(funcional, telefone) VALUES
('9873260', '11987653456'),
('9873261', '11925267849'),
('9873262', '11987382748'),
('9873263', '11943628199'),
('9873264', '11908726381'),
('9873265', '11921821941'),
('9873266', '11959328395'),
('9873267', '11998473934'),
('9873268', '11909382730'),
('9873269', '11982317321'),
('9873270', '11976979002'),
('9873271', '11932849234'),
('9873272', '11903921031'),
('9873273', '11932103219'),
('9873274', '11932198904'),
('9873275', '11904324921'),
('9873276', '11931283128'),
('9873277', '11908293199'),
('9873278', '11923189327'),
('9873279', '11923189315');

INSERT INTO turno(funcional, data_hora_entrada, data_hora_saida, descricao) VALUES
('9873260', '01-11-2021 06:00', '01-11-2021 14:00', 'Horario da manhã'),
('9873261', '02-11-2021 06:00', '02-11-2021 14:00', 'Horario da manhã'),
('9873262', '03-11-2021 15:00', '03-11-2021 21:00', 'Horario da tarde'),
('9873263', '04-11-2021 19:00', '04-11-2021 21:00', 'Horario da noite'),
('9873264', '05-11-2021 15:00', '05-11-2021 21:00', 'Horario da tarde'),
('9873265', '06-11-2021 22:00', '07-11-2021 10:00', 'Horario da madrugada'),
('9873266', '07-11-2021 10:00', '07-11-2021 17:00', 'Horario diurno'),
('9873267', '08-11-2021 10:00', '08-11-2021 17:00', 'Horario diurno'),
('9873268', '09-11-2021 20:00', '10-11-2021 06:00', 'Horario da madrugada'),
('9873269', '10-11-2021 21:00', '11-11-2021 06:00', 'Horario da madrugada'),
('9873270', '11-11-2021 22:00', '12-11-2021 08:00', 'Horario da madrugada'),
('9873271', '12-11-2021 12:00', '12-11-2021 20:00', 'Horario da tarde'),
('9873272', '13-11-2021 12:00', '13-11-2021 20:00', 'Horario da tarde'),
('9873273', '14-11-2021 13:00', '14-11-2021 21:00', 'Horario da tarde'),
('9873274', '15-11-2021 16:00', '15-11-2021 22:00', 'Horario da noite'),
('9873275', '15-11-2021 20:00', '16-11-2021 06:00', 'Horario da madrugada'),
('9873276', '16-11-2021 21:00', '17-11-2021 06:00', 'Horario da madrugada'),
('9873277', '18-11-2021 06:00', '18-11-2021 12:00', 'Horario da manhã'),
('9873278', '19-11-2021 08:00', '19-11-2021 17:00', 'Horario diurno'),
('9873279', '20-11-2021 10:00', '20-11-2021 18:00', 'Horario diurno');

 INSERT INTO servico(id, preco, descricao, nome) VALUES
 ('1', 300.00, 'Aplicação de injeção receitada pelo médico', 'Aplicação de injeção'),
 ('2', 100.00, 'Exame de vista realizado por clinica parceiro', 'Exame de vista'),
 ('3', 0.00, 'Orientação sobre medicamento receitado pelo médico', 'Orientação'),
 ('4', 15.00, 'Orçamento para manipulação de remédios', 'Orçamento de manipulação'),
 ('5', 25.00, 'Manutenção de curativo cirurgico', 'Curativos');

INSERT INTO servico_realizado(codigo, id_servico, cpf_cliente, num_func, data) VALUES
('1', '1', '68043875030', '9873260', '01-10-2021'),
('2', '2', '63191822020', '9873261', '02-10-2021'),
('3', '3','00559460031', '9873262', '03-10-2021'),
('4', '4', '96669265042', '9873263', '04-10-2021'),
('5', '5', '70742547035', '9873264', '05-10-2021'),
('6', '1', '39531904073', '9873261', '06-10-2021'),
('7', '2', '11980749060', '9873262', '07-10-2021'),
('8', '3', '76068362051', '9873263', '08-10-2021'),
('9', '4', '29304490049', '9873264', '09-10-2021'),
('10', '5', '19558162043', '9873261', '10-10-2021'),
('11', '1', '71042853002', '9873262', '11-10-2021'),
('12', '2', '52781063010', '9873263', '12-10-2021'),
('13', '3', '25879781062', '9873264', '13-10-2021'),
('14', '4', '59931225017', '9873261', '14-10-2021'),
('15', '5', '43254364352', '9873262', '15-10-2021'),
('16', '1', '65424321433', '9873263', '15-10-2021'),
('17', '2', '32543635432', '9873264', '15-10-2021'),
('18', '3', '56563342147', '9873261', '15-10-2021'),
('19', '4', '32424521467', '9873262', '15-10-2021'),
('20', '5', '59234125017', '9873263', '15-10-2021');

INSERT INTO compra(cpf_cliente, codigo_compra, num_func, total, data, forma_pagamento, desconto) VALUES
('68043875030', '1', '9873265', 200.00, '01-10-2021', 'Dinheiro', 50.00),
('63191822020', '2', '9873266', 100.00, '02-10-2021', 'Cartão Débito', 30.00),
('00559460031', '3', '9873267', 500.00, '03-10-2021', 'Cartão Crédito', 250.00),
('96669265042', '4', '9873268', 50.00, '04-10-2021', 'PIX', 10.00),
('70742547035', '5', '9873269', 90.00, '05-10-2021', 'Dinheiro', 81.00),
('39531904073', '6', '9873270', 300.00, '06-10-2021', 'Cartão Débito', 75.00),
('11980749060', '7', '9873265', 400.00, '07-10-2021', 'Cartão Débito', 120.00),
('76068362051', '8', '9873266', 1000.00, '08-10-2021', 'Cartão Crédito', 500.00),
('29304490049', '9', '9873267', 100.00, '09-10-2021', 'PIX', 20.00),
('19558162043', '10', '9873268', 500.00, '10-10-2021', 'Cartão Crédito', 450.00),
('71042853002', '11', '9873269', 250.00, '11-10-2021', 'Dinheiro', 62.5),
('52781063010', '12', '9873270', 50.00, '12-10-2021', 'PIX', 15.00),
('25879781062', '13', '9873265', 150.00, '13-10-2021', 'Cartão Débito', 75.00), 
('59931225017', '14', '9873266', 600.00, '14-10-2021', 'PIX', 120.00),
('43254364352', '15', '9873267', 100.00, '15-10-2021', 'Dinheiro', 25.00),
('65424321433', '16', '9873268', 100.00, '12-10-2021', 'Cartão Débito', 25.00),
('32543635432', '17', '9873269', 90.00, '11-10-2021', 'PIX', 30.00),
('56563342147', '18', '9873270', 100.00, '19-10-2021', 'Cartão Débito', 50.00),
('32424521467', '19', '9873265', 50.00, '21-10-2021', 'Cartão Crédito', 10.00),
('59234125017', '20', '9873266', 100.00, '22-10-2021', 'Dinheiro', 90.00);

INSERT INTO produto(codigo_barras, nome, categoria, preco) VALUES
('10254032902', 'Imovane', 'Remédios', 50.00),
('10254032903', 'Colgate Extreme', 'Higiene', 20.00),
('10254032904', 'Sup. Biotina', 'Estética', 250.00),
('10254032905', 'Ibuprofeno', 'Remédios', 10.00),
('10254032906', 'Atenolol', 'Remédios', 90.00),
('10254032907', 'Rinossoro', 'Remédios', 60.00),
('10254032908', 'Flagyl', 'Remédios', 125.00),
('10254032909', 'Kit Skin Care', 'Cosméticos', 500.00),
('10254032910', 'Escova de Dentes', 'Higiene', 25.00),
('10254032911', 'Rioluzol', 'Remédios', 500.00),
('10254032912', 'Kit Desodorante', 'Higiene', 35.71),
('10254032913', 'Fio Dental', 'Higiene', 10.00),
('10254032914', 'Cefalexina', 'Remédios', 75.00),
('10254032915', 'Creme dental', 'Higiene', 20.00),
('10254032916', 'Buscopan', 'Remédios', 40.00),
('10254032917', 'Dipirona', 'Remédios', 40.00),
('10254032918', 'Agua mineral', 'Outros', 05.00),
('10254032919', 'Aparelho para pressão', 'Outros', 200.00),
('10254032920', 'Simeticona', 'Remédios', 25.00),
('10254032921', 'Enxaguante Bucal', 'Higiene', 25.00);


INSERT INTO compra_produto(codigo_compra, codigo_barras, quantidade) VALUES
('1', '10254032902', 4),
('2', '10254032903', 5),
('3', '10254032904', 2),
('4', '10254032905', 5),
('5', '10254032906', 1),
('6', '10254032907', 5),
('7', '10254032908', 6),
('8', '10254032909', 2),
('9', '10254032910', 4),
('10', '10254032911', 1),
('11', '10254032912', 7),
('12', '10254032913', 5),
('13', '10254032914', 2),
('14', '10254032915', 2),
('15', '10254032916', 3),
('16', '10254032917', 2),
('17', '10254032918', 1),
('18', '10254032919', 2),
('19', '10254032920', 3),
('20', '10254032921', 1);


INSERT INTO fornecedor(cnpj, email, endereco, razao_social) VALUES
('70515314000102', 'drogamil@email.com', 'Rua vinte, 34', 'Drogamil fornecimentos ltda.'),
('48815416000194', 'higilife@email.com', 'Rua Padre Milton, 42', 'Higiene life s/a'),
('92986592000180', 'remlog@email.com', 'Avenida Pastoreio, 1001', 'Logistica remedios'),
('32889432894322', 'drogavida@email.com', 'Estrada José, 50', 'Drogavida suplementos'),
('43234232342411', 'higimil@email.com', 'Avenida Lua, 2000', 'Higiene Mil fornecimentos'),
('91212323121552', 'vidamaxima@email.com', 'Rua Mil, 300', 'Vida maxima logistica'),
('35243543542323', 'agualifeg@email.com', 'Rua China, 1001', 'Agua life abastecimentos'),
('65746764755644', 'drogaalig@email.com', 'Avenida Alemanha, 101', 'Droga lig'),
('87657865367535', 'drogabem@email.com', 'Avenida Italia, 11', 'Droga bem serviços'),
('42314214235654', 'higividag@email.com', 'Avenida Russia, 235', 'Higi vida fornecimentos'),
('23416346453673', 'higilog@email.com', 'Rua Croacia, 34', 'Higi logistica'),
('45356435643354', 'colorvida@email.com', 'Rua Omã, 543', 'Color vida suprimentos'),
('21342142154326', 'drogavinte@email.com', 'Avenida Finlandia, 1564', 'Droga Vinte fornecimentos'),
('32141342154325', 'higivinte@email.com', 'Estrada Noruega, 52', 'Higi Vinte fornecimentos'),
('42314324343215', 'drogax@email.com', 'Avenida Dinamarca, 2000', 'Droga x logistica'),
('32131323214532', 'higix@email.com', 'Rua Belgica, 300', 'Higi x fornecimentos'),
('56436436435523', 'logdroga@email.com', 'Avenida Paris, 1423', 'Logistica drogarias ltda.'),
('31232113213254', 'loghigi@email.com', 'Avenida França, 13', 'Logistica higi ltda.'),
('65436356543231', 'xdroga@email.com', 'Avenida Espanha, 1201', 'X drogarias s/a'),
('64536436543654', 'xhigi@email.com', 'Avenida Barcelona, 1501', 'X higi s/a');

INSERT INTO fornecedor_telefones(cnpj_forn, telefone) VALUES
('70515314000102', '11252423212'),
('48815416000194', '11242321245'),
('92986592000180', '11202921023'),
('32889432894322', '11252423213'),
('43234232342411', '11242321244'),
('91212323121552', '11202921025'),
('35243543542323', '11252423216'),
('65746764755644', '11242321247'),
('87657865367535', '11202921088'),
('42314214235654', '11252423219'),
('23416346453673', '11242321240'),
('45356435643354', '11202921031'),
('21342142154326', '11252423423'),
('32141342154325', '11242321654'),
('42314324343215', '11202921076'),
('32131323214532', '11252423634'),
('56436436435523', '11242321321'),
('31232113213254', '11202921086'),
('65436356543231', '11252423243'),
('64536436543654', '11242321123');

INSERT INTO solicitacao_produto(num_func, numero_pedido, codigo_barras, cnpj_forn, quantidade, data_de_validade, data_solicitacao, valor_total)
VALUES
('9873271', '100000', '10254032915', '70515314000102', 2, '12-11-2029', '10-11-2021', 1200.00),
('9873272', '100001', '10254032914', '92986592000180', 5, '02-01-2022', '05-11-2021', 450.00),
('9873271', '100002', '10254032913', '48815416000194', 10, '15-11-2025', '03-12-2021', 100.00),
('9873272', '100003', '10254032902', '70515314000102', 1, '01-01-2029', '10-01-2021', 40.00),
('9873271', '100004', '10254032903', '92986592000180', 2, '02-02-2022', '05-02-2021', 30.00),
('9873272', '100005', '10254032904', '48815416000194', 3, '15-03-2025', '03-03-2021', 600.00),
('9873271', '100006', '10254032905', '70515314000102', 4, '12-04-2029', '10-04-2021', 30.00),
('9873272', '100007', '10254032906', '92986592000180', 5, '02-05-2022', '05-05-2021', 400.00),
('9873271', '100008', '10254032907', '48815416000194', 6, '15-06-2025', '03-06-2021', 300.00),
('9873272', '100009', '10254032908', '70515314000102', 7, '12-07-2029', '10-07-2021', 700.00),
('9873271', '100010', '10254032909', '92986592000180', 8, '02-08-2022', '05-08-2021', 3000.00),
('9873272', '100011', '10254032910', '48815416000194', 9, '15-09-2025', '03-09-2021', 200.00),
('9873271', '100012', '10254032911', '70515314000102', 10, '12-10-2029', '10-10-2021', 4000.00),
('9873272', '100013', '10254032912', '92986592000180', 11, '02-11-2022', '05-11-2021', 300.00),
('9873271', '100014', '10254032916', '48815416000194', 12, '15-12-2025', '03-12-2021', 400.00),
('9873272', '100015', '10254032917', '70515314000102', 13, '12-01-2029', '10-01-2021', 3750.00),
('9873271', '100016', '10254032918', '92986592000180', 14, '02-02-2022', '05-02-2021', 50.00),
('9873272', '100017', '10254032919', '48815416000194', 15, '15-03-2025', '03-03-2021', 2200.00),
('9873271', '100018', '10254032920', '48815416000194', 16, '15-04-2025', '03-04-2021', 300.00),
('9873272', '100019', '10254032921', '48815416000194', 17, '15-05-2025', '03-05-2021', 350.00);
