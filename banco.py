from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine=create_engine('sqlite:///testeDB.db')

l=[]

with engine.connect() as con:
    a=text('''select * from User''')
    b=con.execute(a).all()
    # for registro in b:
    #     a={'id':registro[0],'nome':registro[1]}
    #     l.append(a)

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