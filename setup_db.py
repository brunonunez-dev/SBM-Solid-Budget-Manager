import os
import time
from datetime import date
from src.database import engine, Base, SessionLocal
from src.models import Transaction
from src.services import create_transaction_service

def setup_and_test():
    print("Iniciando Validação da Arquitetura...")
    os.makedirs("./data", exist_ok=True)
    time.sleep(0.2)
    print("Criando Tabelas...")
    Base.metadata.create_all(bind=engine)

    db=SessionLocal()
    try:
        print("Testando Camada de Serviço...")
        new_transaction = create_transaction_service(
            db=db,
            description="Teste de Arquitetura",
            value=1254.74,
            transaction_type="Despesa",
            category="Alimentação",
            date_obj=date.today()
        )
        print(f"""
        OK! Nova transação criada:
        ID: {new_transaction.id}
        Descrição: {new_transaction.description}
        Valor: {new_transaction.value}
        Tipo de Transação: {new_transaction.transaction_type}
        Categoria: {new_transaction.category}
        Data de Criação: {new_transaction.date}""")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    setup_and_test()



