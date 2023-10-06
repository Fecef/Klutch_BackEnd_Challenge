# Klutch Back-End Challenge

---

# Instalação

### Passo-a-passo

1. Criar um ambiente de desenvolvimento virtual.

```bash
python -m venv venv
```

2. Ativar o ambiente virtual.

```bash
# Windows
source ./venv/Scripts/activate

# Mac ou Linux
source ./venv/bin/activate
```

3. Instalar os pacotes necessário.

```bash
pip install -r requirements.txt
```

4. Crie um arquivo **.env** na raíz do projeto e preencha com os valores listados.

```bash
# .env.example
# Conexão com Banco de Dados
SECRET_KEY=secretkey
POSTGRES_USERNAME=postgres_admin_user
POSTGRES_PASSWORD=postgres_admin_password
POSTGRES_DB_NAME=database_name
POSTGRES_DB_HOST=localhost
POSTGRES_PORT=dabase_port
DEBUG=True
```

# Atenção!

### Para prosseguir é necessário ter pré-criado um banco de dados com o nome idêntico ao que foi inserido no campo "database_name" do seu .env

### Prosseguindo...

5. Realizar as migrações para o banco de dados.

```bash
python manage.py migrate
```

6. Executar o servidor local.

```bash
python manage.py runserver
```

# Django Admin
```bash
# Credências de Acesso
Username: klutch
password: 1234
url: http://127.0.0.1:8000/admin/
```

# Documentação da API

```bash
url: http://127.0.0.1:8000/api/docs/
````
