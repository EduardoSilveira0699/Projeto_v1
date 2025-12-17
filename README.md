# 🗂️ Gerenciador de Tarefas — Python + MySQL

Projeto de **Gerenciador de Tarefas em linha de comando**, desenvolvido com foco em **boas práticas de backend**, organização de código, acesso a banco de dados e evolução profissional.

Este projeto faz parte de um processo de aprendizado estruturado, evoluindo do básico até conceitos mais próximos do mercado, como **arquitetura em camadas, logs e testes automatizados**.

---

## 🎯 Objetivo do Projeto

Demonstrar, de forma prática:

* Organização de um projeto Python profissional
* Separação de responsabilidades (MVC simplificado)
* Conexão segura com banco de dados MySQL
* Boas práticas de validação e tratamento de erros
* Evolução incremental do código (níveis)

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **MySQL**
* **mysql-connector-python**
* **python-dotenv**
* **pytest** (testes automatizados)
* **logging** (logs profissionais)
* **Arquitetura MVC simplificada**
* **Ambiente virtual (venv)**

---

## 📌 Funcionalidades

* ✔ Criar nova tarefa
* ✔ Listar tarefas cadastradas
* ✔ Atualizar status da tarefa
* ✔ Deletar tarefa
* ✔ Validação de dados
* ✔ Logs de execução e erros
* ✔ Testes automatizados
* ✔ Conexão segura com banco usando `.env`
* ✔ Estrutura modular e escalável

---

## 📂 Estrutura do Projeto

```text
Projeto_v1/
│
├── controllers/
│   └── tarefa_controller.py
│
├── services/
│   └── tarefa_service.py
│
├── repositories/
│   └── tarefa_repository.py
│
├── database/
│   └── conexao.py
│
├── models/
│   └── tarefa.py
│
├── utils/
│   ├── logger.py
│   └── validacoes.py
│
├── tests/
│   └── test_tarefas.py
│
├── venv/
│
├── .env               # CONFIGURAÇÕES PRIVADAS (NÃO versionar)
├── .env.example       # Modelo de configuração
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙️ Instalação e Configuração

### 1️⃣ Criar e ativar o ambiente virtual (Windows)

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=tarefas_db
```

⚠️ **Nunca envie o arquivo `.env` para o GitHub.**
Use sempre o `.env.example` como referência.

---

## 🗄️ Configuração do Banco de Dados

### Criar o banco:

```sql
CREATE DATABASE tarefas_db;
```

### Criar a tabela:

```sql
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    status ENUM('pendente', 'concluida') DEFAULT 'pendente'
);
```

---

## ▶️ Executando o Programa

Com o ambiente virtual ativado:

```bash
python main.py
```

Menu exibido no terminal:

```text
==== Gerenciador de Tarefas ====

1 - Criar tarefa
2 - Listar tarefas
3 - Atualizar status
4 - Deletar tarefa
5 - Sair
```

---

## 🧪 Executando os Testes

```bash
pytest
```

Os testes validam:

* Criação de tarefas
* Validação de dados
* Atualização de status inválido
* Regras de negócio

---

## 🧩 Arquitetura e Organização

O projeto segue uma **arquitetura em camadas**, facilitando manutenção e evolução:

* **models/** → entidades do domínio
* **repositories/** → acesso ao banco de dados
* **services/** → regras de negócio
* **controllers/** → orquestração das operações
* **utils/** → validações e logs
* **main.py** → ponto de entrada da aplicação

---

## 📈 Evolução do Projeto

* **v1.0** → CRUD básico em Python + MySQL
* **v2.0** → Arquitetura em camadas, logs e testes automatizados
* **v3.0 (planejado)** → API REST com FastAPI

---

## 👤 Autor

**Eduardo Silveira da Silva**
Estudante de Análise e Desenvolvimento de Sistemas
Foco em backend, automação, Python e SQL
Apaixonado por aprender, resolver problemas e evoluir continuamente 🚀

---

## 📄 Licença

Este projeto é livre para fins educacionais.
Sinta-se à vontade para clonar, estudar, testar e propor melhorias.
