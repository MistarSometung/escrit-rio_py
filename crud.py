import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

def Create():
   sql = """
         CREATE TABLE IF NOT EXISTS clientes(
         id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
         nome TEXT NOT NULL,
         cnpj TEXT NOT NULL,
         insc TEXT NOT NULL,
         endereço TEXT NOT NULL,
         numero TEXT NOT NULL,
         bairro TEXT NOT NULL,
         cep TEXT NOT NULL,
         municipio TEXT NOT NULL,
         uf TEXT NOT NULL,
         phone TEXT NOT NULL,
         email TEXT)
         """
   
   cur.execute(sql)
   con.commit()
   
   

def Inserir(nome, cnpj, insc, endereço, numero, bairro, cep, municipio, uf, phone, email):
   
   sql = """
         INSERT INTO clientes(nome, cnpj, insc, endereço, numero, bairro, cep, municipio, uf, phone, email)
         VALUES('{}', '{}', '{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')
         """.format(nome, cnpj, insc, endereço,numero, bairro, cep, municipio, uf, phone, email)
         
   cur.execute(sql)
   con.commit()
   
   
