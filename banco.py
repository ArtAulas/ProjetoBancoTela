from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine=create_engine('sqlite:///testeDB.db')

def get_all():
    with engine.connect() as con:
      q=text('''select * from User''')
      b=con.execute(q).all()
      l=[]
      for registro in b:
          a={'id':registro[0],'nome':registro[1],'ra':registro[2],'curso':registro[3]}
          l.append(a)
    return l


'''
create table User(
  id integer primary key autoincrement,
  nome text,
  ra integer unique,
  curso text
)
'''

'''
insert into User(nome,ra,curso)
values('Arthur',2302331,'SI'),('Bárbara',1873810,'ADS'),('Camily',1562037,'GTI'),('Roberto',1389021,'SI'),('José',2204781,'ADS')
'''