import sqlite3

# Criando banco e conectando a banco
#banco2 = sqlite3.connect(':memory:')
banco2 = sqlite3.connect('CursoPythonR1')
# Criando Cursor
cursor = banco2.cursor()
# Criando tabela Funcionarios (Codigo, PrimeiroNome,
# SegundoNome, UltimoNome,
# DataNasci, CPF, RG, Endereco, CEP,
# Cidade, Fone, CodigoDepartamento,
# Funcao, Salario)

#cursor.execute("CREATE TABLE Funcionarios(Codigo integer,PrimeiroNome text,SegundoNome text,UltimoNome text,DataNascimento integer,CPF integer,RG integer,Endereço text,CEP integer,Cidade text,Fone integer,CodigoDepartamento integer,Funcao text,Salario real)")
#banco2.commit()
listafuncionarios = [('1','A','A','A','03/03/03','123456789-9','412356789-9','moraes 149','04040010','São Paulo','(11)57899462','2','Garçom','3.000.00'),
                     ('2','B','B','B','04/03/03','123456789-8','412356789-8','moraes 148','04040020','São Paulo','(11)57896000','1','TI','5.000.00'),
                    ('3','C','C','C','05/03/03','123456789-7','412356789-7','moraes 147','04040030','São Paulo','(11)57899400','2','Garçom','3.000.00'),
                     ('4','D','D','D','06/03/03','123456789-6','412356789-6','moraes 146','04040040','São Paulo','(11)57899460','3','RH','3.500.00'),
                     ('5','E','E','E','07/03/03','123456789-5','412356789-5','moraes 145','04040050','São Paulo','(11)57899461','4','Recepcionista','1.800.00'),
                     ('6','F','F','F','08/03/03','123456789-4','412356789-4','moraes 144','04040060','São Paulo','(11)57899100','4','Recepçionista','1.800.00'),
                     ('7','G','G','G','09/03/03','123456789-3','412356789-3','moraes 143','04040070','São Paulo','(11)57899410','1','TI','5.000.00'),
                     ('8','H','H','H','02/03/03','123456789-2','412356789-2','moraes 142','04040080','São Paulo','(11)57199462','5','Segurança','2.500.00'),
                     ('9','I','I','I','01/03/03','123456789-1','412356789-1','moraes 141','04040090','São Paulo','(11)57109462','2','Garçom','3.000.00'),
                     ('10','J','J','J','10/03/03','123456789-0','412356789-0','moraes 140','04040071','São Paulo','(11)60899462','6','Gerente','6.000.00')]

#cursor.execute("DROP TABLE Funcionarios")
#cursor.executemany("""INSERT INTO Funcionarios VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",listafuncionarios)
#banco2.commit()
#cursor.execute("SELECT * FROM Funcionarios")
#print(cursor.fetchall())

# Criar Tabela Departamentos (Codigo, Nome,
# Localizacao,
# CodigoFuncionarioGerente)


#cursor.execute("CREATE TABLE Departamentos(Codigo integer,Nome text,Localizacao text,CodigoFuncionáraroGerente integer)")
#banco2.commit()

listadepartamentos = [('1','TI','São Paulo','6'),
                      ('2','Salão','São Paulo','6'),
                      ('3','Escritório','São Paulo','6'),
                      ('4','Recepção','São Palo','6'),
                      ('5','Empresa','São Paulo','6')]

#cursor.execute("DROP TABLE Departamentos")
#cursor.executemany("""INSERT INTO Departamentos VALUES(?,?,?,?)""",listadepartamentos)
#banco2.commit()
#cursor.execute("SELECT * FROM Departamentos")
#print(cursor.fetchall())

# Resposta (a)
#cursor.execute("SELECT PrimeiroNome, SegundoNome From Funcionarios ORDER BY UltimoNome ASC")
#print(cursor.fetchall())

# Resposta (b)
#cursor.execute("SELECT * FROM Funcionarios ORDER BY Cidade ASC")
#print(cursor.fetchall())

# Resposta (c)
#cursor.execute("SELECT * FROM Funcionarios WHERE Salario > '1.000.00' ORDER BY PrimeiroNome,SegundoNome,UltimoNome ")
#print(cursor.fetchall())

# Resposta (d)
#cursor.execute("SELECT DataNascimento, PrimeiroNome FROM Funcionarios ORDER BY DataNascimento ASC")
#print(cursor.fetchall())

# Resposta (e)
#sql = """SELECT SUM(Salario) FROM Funcionarios"""
#cursor.execute(sql)
#print(cursor.fetchall())

# Resposta(F)
#sql = """SELECT Funcionarios.PrimeiroNome, Departamentos.Nome,Funcionarios.Funcao
#FROM Departamentos INNER JOIN Funcionarios ON Funcionarios.CodigoDepartamento = Departamentos.Codigo """
#cursor.execute(sql)
#print(cursor.fetchall())

# Resposta(g)
#sql = """SELECT COUNT(Codigo) FROM Funcionarios"""
#cursor.execute(sql)
#print(cursor.fetchall())

#Resposta(H)
#sql = """SELECT Departamentos.Nome, Funcionarios.PrimeiroNome
#FROM Funcionarios INNER JOIN Departamentos ON Departamentos.Codigo = Funcionarios.CodigoDepartamento  ORDER BY Departamentos.Nome,Funcionarios.PrimeiroNome ASC"""
#cursor.execute(sql)
#print(cursor.fetchall())