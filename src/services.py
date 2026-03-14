from sqlalchemy.orm import Session
from decimal import Decimal
from datetime import date
from src.models import Transaction
from src.repository import save_transaction_repository, get_all_transactions_repository

def create_transaction_service(db:Session, description:str, value:float, transaction_type:str, category:str, date_obj:date):
    """
    Camada de Serviço: (Lógica de Negócio)
    """
    if value <= 0:
        raise ValueError("O valor da transação deve ser maior que zero.")
    
    value_decimal = Decimal(str(value))
    
    new_transaction = Transaction(
        description=description,
        value=value,
        transaction_type=transaction_type,
        category=category,
        date=date_obj
    )
    return save_transaction_repository(db, new_transaction)

def get_transactions_service(db:Session):
    """
    Recupera a lista de Transações.
    """
    return get_all_transactions_repository(db)
