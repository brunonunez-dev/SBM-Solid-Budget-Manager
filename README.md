# SBM-Solid-Budget-Manager
Sistema completo de gestão financeira com Python, Streamlit e SQLAlchemy. Focado em arquitetura limpa e segurança.
# 💰 Gerenciador Financeiro

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


## 📋 Lista de Tarefas
- [x] **Fundação**
    - [x] Configuração do ambiente virtual e Git.
    - [x] Definição da arquitetura de pastas.
- [] **Configuração do Banco de Dados (database.py) (Em Progresso)**
    - [ ] Configuração do Engine SQLAlchemy (SQLite).
    - [ ] Criação do Modelo de Dados Transacao.
    - [ ] Implementação da função criar_banco.
- [] **Implementação do CRUD (crud.py)**
    - [] Função para salvar nova transação.
    - [] Função para listar todas as transações.
    - [] Função para deletar transação por ID.
- [] **Lógica de Negócio e Validações (services.py)**
    - [] Implementação de validações de entrada (ex: impedir valores nulos ou negativos).
    - [] Funções de cálculo de saldo total (Receitas - Despesas).
    - [] Agrupamento de gastos por categoria para o Dashboard.
    - [] Implementação de lógica de exportação (CSV/PDF).
- [] **Interface do Usuário (app.py - Streamlit)**
    - [] Criação do formulário de entrada de dados.
    - [] Desenvolvimento da tabela de exibição de histórico.
    - [] **Dashboard Visual:**
        - [] Gráfico de pizza por categoria.
        - [] Gráfico de evolução mensal de gastos.
    - [] Filtros de data e tipo de transação.
- [] **API e Segurança**
    - [] Migração da lógica para FastAPI.
    - [] **Sistema de Autenticação:**
        - [] Cadastro de usuários com Hash de senha (BCrypt).
        - [] Login com Token JWT.
    - [] Proteção de rotas (o usuário só vê as próprias transações).
    - [] Documentação automática da API com Swagger/OpenAPI.
- [] **Qualidade e Deploy**
    - [] Escrita de testes unitários com pytest.
    - [] Implementação de logs de erro.
    - [] Deploy da aplicação (Streamlit Cloud ou Docker).



## 🧠 Decisões de Design

Nesta seção, detalho as escolhas técnicas feitas para garantir que o **SBM** seja robusto e escalável.

> ### Planejamento:
- **Integridade Monetária**: Uso do tipo `Numeric` para manipulação de valores financeiros, garantindo precisão decimal.

> ### Desenvolvimento:

- **Criação da Engine**: `check_same_thread": False` permite que o SQLite trabalhe com o modelo assíncrono do FastAPI/Streamlit.
- **Configuração de Sessão**: `autoflush=False` e `autocommit=False` para garantir que as alterações só sejam persistidas após validações completas na camada de serviços.
