import pandas as pd  
import sqlite3
import numpy as np 
# from django.contrib.auth.hashers import make_password, check_password

df = pd.read_excel ("a.xlsx")
lista=[]
columnas=len(df.columns)
for i in range (columnas):
    x = pd.DataFrame(df, columns= [df.columns[i]])
    x = np.array( x.values)
    lista.append(x)


filas=len(lista[0])
nombre=lista[0]
cmp_0=lista[1]
esp=lista[2]
repre=lista[3]
# print(nombre)


con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
for i in range(filas):
	n=nombre[i][0]
	c=int(cmp_0[i][0])
	e=esp[i][0]
	r=repre[i][0]
	
	cur.execute("insert into rest_app_medicos values (?, ?, ?, ?, ?)", (i+1,n,c,e,r))

	con.commit()


con.close()