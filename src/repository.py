from sqlalchemy.orm import Session
from src.models import Transaction

def save_transaction_repository(db:Session, transaction_obj:Transaction):
    """
    Camada de Repositório: Responsável apenas por salvar o objeto no banco.
    """
    try:
        db.add(transaction_obj)
        db.commit()
        db.refresh(transaction_obj)
        return transaction_obj
    except Exception as e:
        db.rollback()
        raise e