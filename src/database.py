from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = 'sqlite:///./data/sbm_database.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    value = Column(Numeric(10, 2), nullable=False, asdecimal=True)
    transaction_type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)

def create_database():
    Base.metadata.create_all(bind=engine)