from sqlalchemy import Column, Integer, String, Numeric, Date
from src.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    value = Column(Numeric(10, 2, asdecimal=True), nullable=False)
    transaction_type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)