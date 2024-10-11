from sqlalchemy  import Column , String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base

class Usuario(Base):
    
    __tablename__="usuarios"
    
    id= Column (Integer,primary_key = True,autoincrement=True)
    nome = Column (String(250))
    email = Column (String(250),unique=True)
    senha= Column(String(250))


    def __init__(self, nome:str,email:str,senha:str)->None:
        self.nome = nome 
        self.email = email
        self.senha = senha



Base.metadata.create_all(bind=db)

