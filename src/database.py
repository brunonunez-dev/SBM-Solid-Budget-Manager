from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


DATABASE_URL = 'sqlite:///./data/sbm_database.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@contextmanager
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Cria tabelas no banco de dados caso elas não existam"""
    import src.models
    Base.metadata.create_all(bind=engine)