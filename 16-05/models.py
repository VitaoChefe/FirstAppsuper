from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///list_view_livro.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(40), nullable=False, index=True, unique=True)
    autor = Column(String(40), nullable=False, index=True)
    descricao = Column(String(255), nullable=False, index=True)
    categoria = Column(String(255), nullable=False, index=True)

    def __repr__(self):
        return '<Livro {}>'.format(self.titulo, self.autor, self.descricao, self.categoria)

    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    def serialize(self):
        livro = {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'descricao': self.descricao,
            'categoria': self.categoria,
        }
        return livro
def init_db():
    Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    init_db()