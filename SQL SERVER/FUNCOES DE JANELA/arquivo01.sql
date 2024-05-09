--ex01

SELECT 
	f.Pnome,
	f.Datanasc,
	f.Salario,
	SUM(f.Salario) OVER(ORDER BY f.Datanasc)
FROM FUNCIONARIO f;

--ex02

SELECT 
	f.Pnome,
	f.Salario,
	f.Dnr ,
	AVG(f.Salario) OVER(PARTITION BY f.Dnr) 
FROM FUNCIONARIO f

--ex03

SELECT 
	f.Pnome,
	COUNT(d.Fcpf) AS QUANTIDADE_DEP,
	RANK() OVER(ORDER BY COUNT(d.Fcpf) desc) AS RANQUE
FROM DEPENDENTE d 
LEFT JOIN FUNCIONARIO f
ON d.Fcpf = f.Cpf 
GROUP BY  f.Pnome

--ex04

SELECT tabela.Pnome 
FROM (SELECT 
	f.Pnome,
	COUNT(d.Fcpf) AS QUANTIDADE_DEP,
	RANK() OVER(ORDER BY COUNT(d.Fcpf) desc) AS RANQUE
FROM DEPENDENTE d 
LEFT JOIN FUNCIONARIO f
ON d.Fcpf = f.Cpf 
GROUP BY  f.Pnome
) AS tabela
WHERE tabela.RANQUE = 1

