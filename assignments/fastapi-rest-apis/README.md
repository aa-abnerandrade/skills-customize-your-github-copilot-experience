# 📘 Tarefa: Construindo APIs REST com o Framework FastAPI

## 🎯 Objetivo

Desenvolver uma compreensão sólida do framework FastAPI e criar APIs REST funcionais com endpoints para operações CRUD (Create, Read, Update, Delete) usando modelos de dados com Pydantic.

## 📝 Tasks

### 🛠️ Criando uma API Básica com FastAPI

#### Descrição
Crie uma aplicação FastAPI básica que demonstre a estrutura fundamental do framework, incluindo a importação de módulos, criação de uma instância da aplicação e definiçãode um endpoint simples.

#### Requisitos
O programa completo deve:

- Importar `FastAPI` do módulo `fastapi`
- Criar uma instância da aplicação FastAPI chamada `app`
- Definir um endpoint GET na rota `/` que retorne uma mensagem de boas-vindas em formato JSON (por exemplo: `{"message": "Bem-vindo à minha API!"}`)
- Ser executável com `uvicorn main:app --reload`
- Incluir documentação automática acessível em `/docs`

### 🛠️ Implementando Operações CRUD com Modelos Pydantic

#### Descrição
Crie um sistema de gerenciamento de tarefas (TODO list) com endpoints que suportam operações CRUD. Use modelos Pydantic para validação de dados.

#### Requisitos
O programa completo deve:

- Definir um modelo Pydantic `Task` com campos: `id` (int), `title` (str), `description` (str), `completed` (bool)
- Implementar um armazenamento em memória (lista) para as tarefas
- Criar um endpoint GET `/tasks` que retorne todas as tarefas
- Criar um endpoint POST `/tasks` que crie uma nova tarefa e a adicione à lista
- Criar um endpoint GET `/tasks/{id}` que retorne uma tarefa específica por ID
- Criar um endpoint PUT `/tasks/{id}` que atualize uma tarefa existente
- Criar um endpoint DELETE `/tasks/{id}` que remova uma tarefa da lista
- Retornar status apropriados (200, 201, 404, etc.)

### 🛠️ Validação e Tratamento de Erros

#### Descrição
Implemente validação robusta e tratamento de erros em sua API, garantindo que dados inválidos sejam rejeitados com mensagens de erro claras.

#### Requisitos
O programa completo deve:

- Usar validadores Pydantic para garantir que campos obrigatórios sejam preenchidos
- Implementar tratamento de erros para recursos não encontrados (404)
- Retornar mensagens de erro em formato JSON com status codes apropriados
- Validar que IDs são números inteiros positivos
- Retornar uma resposta HTTP 422 quando dados inválidos forem enviados
