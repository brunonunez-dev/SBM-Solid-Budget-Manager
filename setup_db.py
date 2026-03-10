import os
from datetime import date
from src.database import create_database, SessionLocal, DATABASE_URL, engine, Base
from src.crud import create_transaction

def test_database_setup():
    print("Teste de infraestrutura do banco de dados iniciado!")

    db_path = "./data/sbm_database.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Banco de dados antigo removido em {db_path}")


    print("Criacao de tabelas iniciada!")
    create_database()

    print("Validação do create iniciada!")
    db=SessionLocal()
    try:
        nova_transacao=create_transaction(
            db=db,
            description="Teste de Configuração",
            value=1250.00,
            transaction_type="Receita",
            category="Salário",
            date=date.today()
        )
        print(f"Transação {nova_transacao.description} criada!")
        print(f"ID gerado: {nova_transacao.id}")
        print(f"Valor: R$ {nova_transacao.value}, Tipo: {type(nova_transacao.value)}")
        print(f"Tipo da transação: {nova_transacao.transaction_type}")
        print(f"Categoria: {nova_transacao.category}")
        print(f"Data: {nova_transacao.date}")
    except Exception as e:
        print(f"ERRO: {e}")
    finally:
        db.close()

if __name__=="__main__":
    test_database_setup()