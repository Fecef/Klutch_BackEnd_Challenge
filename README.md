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
POSTGRES_USERNAME="preencha com o username do admin do postgreSQL"
POSTGRES_PASSWORD="preencha com o password do admin do postgreSQL"
POSTGRES_DB_NAME=klutch_db
POSTGRES_DB_HOST=localhost
POSTGRES_PORT=5432
DEBUG=True
```

# Atenção!

### Para prosseguir é necessário ter pré-criado um banco de dados com nome "klutch_db"

### Prosseguindo...

5. Realizar as migrações para o banco de dados.

```bash
python manage.py migrate
```

6. Executar o servidor local.

```bash
python manage.py runserver
```

# Django Admin - localserver
Quando o banco de dados é criado, é necessario também criar um novo django-admin.
```bash
# Nessário inserir somente Username e Password
python manage.py createsuperuser
# Local URL
http://127.0.0.1:8000/admin/
```

No caso do servidor externo, o django-admin já está criado.
```bash
# Credências de Acesso
Username: klutch
password: 1234
# Render URL
https://klutch-challenge.onrender.com/admin/
```

# Documentação da API

```bash
# Local URL
http://127.0.0.1:8000/api/docs/
# Render URL
https://klutch-challenge.onrender.com/api/docs/
````
