from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///list_view.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    salario = Column(Integer, nullable=False)
    cargo = Column(Integer, nullable=False)

def __init__(self, nome, salario, cargo):
    self.nome = nome
    self.salario = salario
    self.cargo = cargo

def save(self):
    db_session.add(self)
    db_session.commit()
def delete(self):
    db_session.delete(self)
    db_session.commit()
def serialize(self):
    return {
        'id': self.id,
        'nome': self.nome,
        'salario': self.salario,
        'cargo': self.cargo,
    }
def init_db():
    Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    init_db()