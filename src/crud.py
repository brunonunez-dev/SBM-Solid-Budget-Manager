from sqlalchemy.orm import Session
from src.database import Transaction
from datetime import date

def create_transaction(
    db:Session, 
    description:str,
    value:float,
    type:str,
    category:str,
    date:date
):
    """
    Cria uma nova transação no banco de dados.
    """
    db_transaction = Transaction(
        description=description,
        value=value,
        type=type,
        category=category,
        date=date
    )
    db.add(db_transaction)
    db.commit()

    db.refresh(db_transaction)

    return db_transaction
