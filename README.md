# SBM-Solid-Budget-Manager
Sistema completo de gestão financeira com Python, Streamlite e SQLAlchemy. Focado em arquitetura limpa e segurança.
# 💰 Gerenciador Financeiro Pro

Sistema de gestão financeira pessoal focado em **Integridade de Dados** e **Arquitetura Escalável**.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Interface:** Streamlit (Web UI)
* **Backend/API:** FastAPI (Implementação Futura)
* **Banco de Dados:** SQLite com SQLAlchemy (ORM)
* **Segurança:** BCrypt para senhas e JWT para sessões.

## 🏗️ Arquitetura do Projeto
O projeto segue o padrão de **Separação de Preocupações (SoC)**:
- `src/database.py`: Configuração da conexão e modelos do banco.
- `src/crud.py`: Camada de persistência CRUD(Create, Read, Update, Delete).
- `src/services.py`: Regras de negócio e validações lógicas.
- `src/app.py`: Interface do usuário.

## 🛠️ Como rodar o projeto
(Em breve instruções de instalação...)