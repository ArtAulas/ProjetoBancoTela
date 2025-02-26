from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine=create_engine('sqlite:///testeDB.db')

def get_all():
    with engine.connect() as con:
      q=text('''select * from User''')
      retorno=con.execute(q).all()
      l=[]
      for registro in retorno:
          a={'id':registro[0],'nome':registro[1],'ra':registro[2],'curso':registro[3]}
          l.append(a)
    return l

def insert(dici):
   #dici={'nome':"Nome_Pessoa",'ra':1234567,'curso':"Curso_Pessoa"}
   with engine.connect() as con:
      query=text('''insert into User(nome,ra,curso) values(:nomeQ,:raQ,:cursoQ)''')
      rs=con.execute(query,{'nomeQ':dici['nome'],'raQ':dici['ra'],'cursoQ':dici['curso']})
      con.commit()

def delete(id):
   with engine.connect() as con:
      q=text('delete from User where id='+str(id))
      con.execute(q)
      con.commit()