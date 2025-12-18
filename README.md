# 🍽️ API de Restaurantes - CRUD Completo com FastAPI

## 📋 Descrição do Projeto
Esta é uma atividade prática de desenvolvimento de uma API RESTful completa para gerenciamento de restaurantes, implementando todas as operações CRUD (Create, Read, Update, Delete) utilizando o framework **FastAPI** em Python.

## 🎯 Objetivo
Criar um sistema de gerenciamento de restaurantes que permita:
- Cadastrar novos restaurantes
- Listar todos os restaurantes cadastrados
- Buscar restaurantes específicos
- Atualizar informações de restaurantes
- Remover restaurantes do sistema

## 🛠️ Tecnologias Utilizadas
- **Python 3.7+**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI
- **SQLite** - Banco de dados relacional (para desenvolvimento)

## 📁 Estrutura do Projeto
```
CRUD/
├── main.py              # Aplicação FastAPI principal
├── database.py          # Configuração do banco de dados
├── models.py            # Modelos SQLAlchemy
├── schemas.py           # Schemas Pydantic para validação
├── crud.py              # Operações de banco de dados
├── requirements.txt     # Dependências do projeto
└── restaurantes.db      # Banco de dados SQLite (gerado automaticamente)
```

## 🔧 Instalação e Configuração

### 1. Clonar/Preparar o ambiente
```bash
# Navegar para a pasta do projeto
cd CRUD
```

### 2. Criar e ativar ambiente virtual (venv)
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no PowerShell (Windows)
.\venv\Scripts\Activate

# Ativar no CMD (Windows)
venv\Scripts\activate.bat

# Ativar no Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```
Ou instalar manualmente:
```bash
pip install fastapi uvicorn sqlalchemy
```

### 4. Executar a aplicação
```bash
# Com venv ativado
uvicorn main:app --reload
```

## 🌐 Endpoints da API

### Rotas disponíveis:

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Mensagem de boas-vindas |
| `POST` | `/restaurantes/` | Criar novo restaurante |
| `GET` | `/restaurantes/` | Listar todos os restaurantes |
| `GET` | `/restaurantes/{id}` | Buscar restaurante por ID |
| `PUT` | `/restaurantes/{id}` | Atualizar restaurante |
| `DELETE` | `/restaurantes/{id}` | Deletar restaurante |

## 📖 Documentação Interativa

A API inclui documentação automática gerada pelo FastAPI:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Exemplos de Requisições

### Criar Restaurante (POST /restaurantes/)
```json
{
  "nome": "Sabor Brasileiro",
  "endereco": "Av. Paulista, 1000",
  "tipo_cozinha": "Brasileira",
  "capacidade": 80,
  "descricao": "Restaurante com comida típica do Brasil"
}
```

### Atualizar Restaurante (PUT /restaurantes/{id})
```json
{
  "capacidade": 100,
  "tipo_cozinha": "Nordestina"
}
```

## 🗄️ Modelo de Dados

### Restaurante
- `id` (Integer, Primary Key)
- `nome` (String, obrigatório)
- `endereco` (String, opcional)
- `tipo_cozinha` (String, opcional)
- `capacidade` (Integer, opcional)
- `descricao` (Text, opcional)

## 📊 Funcionalidades Implementadas

- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Validação de dados com Pydantic
- ✅ Banco de dados SQLite com SQLAlchemy
- ✅ Tratamento de erros (404, etc.)
- ✅ Documentação automática
- ✅ Separação de responsabilidades (MVC-like)
- ✅ Paginação nas consultas
- ✅ Ambiente virtual isolado

## 🚀 Como Testar

1. Execute a aplicação com `uvicorn main:app --reload`
2. Acesse http://localhost:8000/docs
3. Use a interface Swagger para testar os endpoints
4. Ou use ferramentas como:
   - **Postman**
   - **cURL**
   - **Insomnia**

## 🔍 Exemplo de Teste com cURL

```bash
# Listar restaurantes
curl -X GET "http://localhost:8000/restaurantes/"

# Criar restaurante
curl -X POST "http://localhost:8000/restaurantes/" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Teste","endereco":"Rua Teste"}'
```

## 📝 Considerações Finais

Este projeto demonstra os conceitos fundamentais do desenvolvimento de APIs REST com FastAPI, incluindo:

1. **Estruturação de projetos** em camadas
2. **Validação de dados** com Pydantic
3. **Operações de banco de dados** com SQLAlchemy
4. **Documentação automática** integrada
5. **Boas práticas** de desenvolvimento Python

## 👨‍🏫 Referência Acadêmica
**Atividade:** Criando o primeiro CRUD completo com FastAPI  
**Capítulo de referência:** 3. FastAPI Tour  
**Professor:** Anthony Irlan Marques Luz

## 📄 Licença
Projeto educacional desenvolvido para fins acadêmicos.

---

**Desenvolvido com ❤️ usando FastAPI**
