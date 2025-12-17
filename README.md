# 🗂️ Gerenciador de Tarefas — Python + MySQL

Projeto de **Gerenciador de Tarefas em linha de comando**, desenvolvido com foco em **boas práticas**, **arquitetura limpa**, **validações**, **testes automatizados** e **organização profissional de código**.

Este projeto evolui por **níveis**, simulando o crescimento real de um sistema backend — desde um CRUD simples até uma aplicação bem estruturada e testável.

---

## 🎯 Objetivo do Projeto

Permitir o **cadastro, listagem, atualização e exclusão de tarefas**, aplicando:

* Separação de responsabilidades
* Regras de negócio isoladas
* Acesso a banco desacoplado
* Testes unitários confiáveis

Projeto ideal para **portfólio**, **estudo de backend** e **preparação para APIs REST**.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **MySQL**
* **mysql-connector-python**
* **python-dotenv**
* **pytest** (testes automatizados)
* **Arquitetura MVC + Service + Repository**
* **Logs estruturados**
* **Ambiente virtual (venv)**

---

## 📌 Funcionalidades

✔ Criar nova tarefa
✔ Listar tarefas cadastradas
✔ Atualizar status da tarefa (`pendente` / `concluido`)
✔ Deletar tarefa
✔ Validações de entrada
✔ Logs de operações e erros
✔ Testes unitários sem dependência do banco

---

## 🧱 Arquitetura do Projeto

O projeto segue uma separação clara de camadas:

* **models/** → Entidades do domínio
* **controllers/** → Interface entre usuário e sistema
* **services/** → Regras de negócio
* **repositories/** → Acesso ao banco de dados
* **database/** → Conexão com MySQL
* **utils/** → Validações e logs
* **views/** → Interface de menu (CLI)
* **tests/** → Testes automatizados

---

## 📂 Estrutura de Pastas

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
├── models/
│   └── tarefa.py
│
├── database/
│   └── conexao.py
│
├── utils/
│   ├── validation.py
│   └── logger.py
│
├── views/
│   └── menu.py
│
├── tests/
│   ├── test_tarefa_controller.py
│   ├── test_tarefa_service.py
│   └── test_validation.py
│
├── .env               # CONFIGURAÇÕES PRIVADAS (NÃO subir no Git)
├── .env.example       # Modelo do .env
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Criar e ativar o ambiente virtual (Windows)

```bash
python -m venv venv
.\venv\Scripts\activate
```

---

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configurar variáveis de ambiente

Crie um arquivo **.env** na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=tarefas_db
```

⚠️ **Nunca envie o arquivo `.env` para o GitHub.**
Use o `.env.example` como referência.

---

## 🗄️ Configuração do Banco de Dados

### Criar o banco

```sql
CREATE DATABASE tarefas_db;
```

### Criar a tabela

```sql
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    status ENUM('pendente', 'concluido') DEFAULT 'pendente'
);
```

---

## ▶️ Executando o Programa

Com o ambiente virtual ativado:

```bash
python main.py
```

Menu exibido:

```text
==== GERENCIADOR DE TAREFAS ====
1 - Criar tarefa
2 - Listar tarefas
3 - Atualizar status
4 - Deletar tarefa
0 - Sair
```

---

## 🧪 Testes Automatizados

O projeto possui **testes unitários completos**, cobrindo:

* Validação de status
* Regras do Service
* Controllers
* Fluxos válidos e inválidos

### Executar os testes

```bash
pytest -v
```

✔ **Resultado atual:** `9 passed`
Todos os testes passam com sucesso.

---

## 📈 Evolução por Níveis

### 🔹 Nível 1

* CRUD básico
* MVC simples
* Conexão direta com banco

### 🔹 Nível 2 (ATUAL)

* Service Layer
* Repository Pattern
* Validações centralizadas
* Testes unitários
* Logs estruturados

### 🔜 Próximo Nível

* Exceptions customizadas
* Paginação e filtros
* API REST com FastAPI
* CI/CD com GitHub Actions

---

## 👤 Autor

**Eduardo S. da Silva**
Estudante de Análise e Desenvolvimento de Sistemas
Backend • Automação • SQL • Python

Apaixonado por resolver problemas com código e evoluir continuamente.

---

## 📄 Licença

Este projeto é livre para estudos, melhorias e contribuições.

Sinta-se à vontade para clonar, testar e evoluir 🚀
