🗂️ Gerenciador de Tarefas — Python + MySQL

Este projeto é um **Gerenciador de Tarefas em linha de comando**, desenvolvido para aplicar e demonstrar conceitos 
fundamentais de programação, organização de projeto, acesso a banco de dados e boas práticas com Python.

O objetivo deste sistema é permitir o cadastro, listagem, atualização e exclusão de tarefas, utilizando uma arquitetura
simples e eficiente.

🚀 Tecnologias Utilizadas

- Python 3.10+
- MySQL
- mysql-connector-python
- python-dotenv
- Arquitetura MVC simplificada
- Ambiente virtual (venv)

📌 Funcionalidades

✔ Criar nova tarefa
✔ Listar tarefas cadastradas
✔ Atualizar status da tarefa (pendente → concluída)
✔ Deletar tarefa
✔ Conexão segura com banco usando `.env`
✔ Estrutura modular (controllers, models, database)

📂 Estrutura do Projeto
Projeto_v1/
│
├── controllers/
│   └── tarefa_controller.py
│
├── database/
│   └── conexao.py
│
├── models/
│   └── tarefa.py
│
├── venv/
│
├── .env               # CONFIGURAÇÕES PRIVADAS (não subir no Git)
├── .env.example       # Modelo para quem baixar o projeto
├── requirements.txt
├── main.py
└── README.md

1️⃣ Criar e ativar o ambiente virtual (Windows)

powershell
python -m venv venv
.\venv\Scripts\activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Configurar o arquivo .env
Crie um arquivo chamado .env na raiz do projeto:

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=tarefas_db

⚠️ Nunca envie este arquivo ao GitHub.
Use o .env.example como modelo.

🗄️ Configuração do Banco de Dados
Crie um banco MySQL com o nome:

tarefas_db

E a tabela:

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    status ENUM('pendente', 'concluida') DEFAULT 'pendente'
);

▶️ Execução do Programa
No terminal (com o venv ativado):

python main.py

Você verá o menu:
==== Gerenciador de Tarefas ====
1. Criar tarefa
2. Listar tarefas
3. Atualizar status
4. Deletar tarefa
0. Sair
Escolha uma opção:

🧩 Funcionamento Interno

O projeto segue uma estrutura modular simples:

models/ → contém as classes de domínio (Tarefa).

controllers/ → contém a lógica das operações no banco.

database/ → responsável pela conexão MySQL.

main.py → ponto de entrada da aplicação.


👤 Autor

Eduardo S. da Silva

Estudante de ADS, desenvolvimento backend, automação e SQL.

Apaixonado por resolver problemas com código e evoluir diariamente.


## 📄 Licença

Este projeto é livre para estudos e melhorias.

Fique à vontade para clonar, testar e sugerir alterações.
