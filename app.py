import streamlit as st
from src.services import create_transaction_service
from datetime import date
from src.database import get_db, init_db

init_db()

st.set_page_config(page_title="SBM - Solid Budget Manager", layout="wide")


st.header("➕ Nova Transação")

with st.form("transaction_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        description = st.text_input("Descrição", placeholder="Ex: Aluguel, Salário...")
        value = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        category = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Saúde", "Moradia", "Salário", "Outros"])

    with col2:
        transaction_type = st.radio("Tipo", ["Receita", "Despesa"])
        date_obj = st.date_input("Data",
         value=date.today(),
         format="DD/MM/YYYY"
        )

    submit = st.form_submit_button("Salvar")

    if submit:
        with get_db() as db:
            try:
                new_tx = create_transaction_service(
                    db=db,
                    description=description,
                    value=value,
                    transaction_type=transaction_type,
                    category=category,
                    date_obj=date_obj
                )
                st.success(f"Transação '{description}' salva com sucesso!")
                st.rerun()
            except ValueError as e:
                st.error(f"Erro de Validação: {e}")
            except Exception as e:
                st.error(f"Erro interno no sistema: {e}")
            finally:
                db.close()