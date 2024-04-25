SELECT f.Pnome, f.Unome
FROM FUNCIONARIO f  
LEFT JOIN  DEPENDENTE d
ON f.Cpf = d.Fcpf 
WHERE d.Sexo  IN (
	SELECT d2.sexo
	FROM DEPENDENTE d2 
	WHERE d2.sexo = 'M'
)


SELECT f.Pnome 
FROM FUNCIONARIO f
WHERE f.Salario > (
	SELECT  AVG(f2.Salario)  
	FROM FUNCIONARIO f2 	
)


SELECT d.Dnome 
FROM DEPARTAMENTO d
WHERE d.Dnumero = ANY (
	SELECT ld.Dnumero 
	FROM LOCALIZACAO_DEP ld
	WHERE ld.Dlocal  = 'Houston' OR ld.Dlocal  = 'Stafford'
)

SELECT f.Pnome, f.Endereco 
FROM FUNCIONARIO f
left join DEPARTAMENTO d 
on f.Dnr = d.Dnumero 
WHERE d.Dnumero   = ANY (
	SELECT ld.Dnumero 
	FROM LOCALIZACAO_DEP ld
	WHERE ld.Dlocal  = 'Houston' OR ld.Dlocal  = 'Stafford'
)


SELECT p.Projnumero, p.Projlocal, d.Dnumero
FROM PROJETO p
join DEPARTAMENTO d 
on p.Dnum = d.Dnumero 
where d.Dnumero in (
	SELECT ld.Dnumero
	FROM LOCALIZACAO_DEP ld 
	where p.Projlocal <> ld.Dlocal
)


SELECT f.Pnome, f.Unome
FROM FUNCIONARIO f  
LEFT JOIN  DEPENDENTE d
ON f.Cpf = d.Fcpf 
WHERE d.Fcpf = (
	SELECT MAX(d.)
	from DEPENDENTE d2 

)

SELECT f.Pnome, f.Unome
FROM FUNCIONARIO f
WHERE EXISTS (
    SELECT 1
    FROM DEPENDENTE d
    WHERE d.Fcpf = f.Cpf
    GROUP BY d.Fcpf
  
    
   CREATE TABLE R(
    EventoID INT primary key 
    ,Inicio datetime NOT NULL
    ,fim datetime not null
    );
    
   
INSERT INTO GabrielOliveiraDoSGBD.dbo.R
(EventoID, Inicio, fim)
VALUES(1, '16/04/2024 20:00', '16/04/2024 22:00');

INSERT INTO GabrielOliveiraDoSGBD.dbo.R
(EventoID, Inicio, fim)
VALUES(2, '16/04/2024 22:00', '17/04/2024 04:00');

INSERT INTO GabrielOliveiraDoSGBD.dbo.R
(EventoID, Inicio, fim)
VALUES(3, '17/04/2024 10:00', '17/04/2024 14:00');

INSERT INTO GabrielOliveiraDoSGBD.dbo.R
(EventoID, Inicio, fim)
VALUES(4, '17/04/2024 12:00', '17/04/2024 16:00');

INSERT INTO GabrielOliveiraDoSGBD.dbo.R
(EventoID, Inicio, fim)
VALUES(5, '17/04/2024 22:00', '18/04/2024 02:00');

SELECT SUM(DATEDIFF(HOUR, Inicio, fim)) as duracao_total 
FROM R 
WHERE inicio < cast(GETDATE()as date)
AND fim > cast(dateadd(day,-1, GETDATE()) as date)


SELECT SUM(DATEDIFF(HOUR, Inicio, fim)) as duracao_total 
FROM R 
WHERE inicio < cast('2024-04-18' as date)
AND fim > cast('2024-04-17' as date)


SELECT LEFT(UPPER(f.Pnome),  3) + '-' + RIGHT(RTRIM(f.cpf) ,3) 
FROM FUNCIONARIO f 

SELECT d.Dnome, d.Data_inicio_gerente, f.Pnome, DATEADD(year,5,d.Data_inicio_gerente) 
FROM DEPARTAMENTO d 
left join FUNCIONARIO f 
on f.Cpf = d.Cpf_gerente 

    
 


