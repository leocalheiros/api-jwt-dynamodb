# API JWT com DynamoDB no AWS Lambda

Este é um exemplo de uma API simples que utiliza o AWS Lambda, Flask e DynamoDB para implementar recursos de autenticação e gerenciamento de usuários com tokens JWT. A API possui as seguintes funcionalidades:

- **Criar Usuário:** Cria um novo usuário no banco de dados.
- **Listar Usuários:** Lista todos os usuários armazenados no banco de dados (requer autenticação).
- **Deletar Usuário:** Remove um usuário do banco de dados (requer autenticação).
- **Login:** Autentica um usuário e fornece um token JWT para autorização subsequente.

## Pré-requisitos

Antes de usar a API, certifique-se de ter:

- Configurado um ambiente AWS Lambda.
- Configurado uma tabela DynamoDB chamada `TestUsersTable` (no código do projeto utilizo o DynamoDB local, certifique-se de quando subir para a AWS, remover o endpoint local).
- Empacotado corretamente as dependências da aplicação para implantação no AWS Lambda.
- Configurado a variável de ambiente `JWT_SECRET_KEY` com uma chave secreta para geração de tokens JWT (recomendado armazenar essas variáveis em um arquivo .env).

## Estrutura de Diretórios

- `lambda_handler.py`: Ponto de entrada da AWS Lambda.
- `src/controllers/`: Controladores da API.
- `src/models/`: Modelo de dados para interagir com o DynamoDB.
- `src/views/`: Funções de visualização para formatar respostas.
- `src/controllers/jwt_controller.py`: Controlador para geração e validação de tokens JWT.
- `src/controllers/user_controller.py`: Controlador para operações de criação, listagem e exclusão de usuários.
- `src/controllers/login_controller.py`: Controlador para a rota de autenticação.
- `src/views/user_view.py`: Funções de visualização para formatar respostas JSON.
- `src/models/user_model.py`: Modelo de usuário para interagir com o DynamoDB.

## Endpoints da API

### Criar Usuário

- **URL**: `/user/create-user`
- **Método**: `POST`
- **Headers**: Nenhum
- **Corpo da Requisição**: JSON contendo `user_id`, `email` e `senha` do novo usuário.
- **Resposta de Sucesso**: Status HTTP 201 (Criado) com a mensagem `Usuário criado com sucesso!`.

### Listar Usuários

- **URL**: `/user/get-users`
- **Método**: `GET`
- **Headers**: `Authorization` (Token JWT) e `email` (E-mail do usuário autenticado).
- **Corpo da Requisição**: Nenhum
- **Resposta de Sucesso**: Status HTTP 200 (OK) com a lista de todos os usuários.

### Deletar Usuário

- **URL**: `/user/delete-user/<user_id>`
- **Método**: `DELETE`
- **Headers**: `Authorization` (Token JWT) e `email` (E-mail do usuário autenticado).
- **Corpo da Requisição**: Nenhum
- **Resposta de Sucesso**: Status HTTP 200 (OK) com a mensagem `Usuário deletado com sucesso!`.

### Login

- **URL**: `/auth/login`
- **Método**: `POST`
- **Headers**: Nenhum
- **Corpo da Requisição**: JSON contendo `email` e `senha` do usuário.
- **Resposta de Sucesso**: Status HTTP 200 (OK) com o token JWT gerado.

## Configuração no AWS Lambda

- Certifique-se de configurar o ambiente AWS Lambda com permissões adequadas para acessar a tabela DynamoDB.
- Configure as variáveis de ambiente, incluindo `JWT_SECRET_KEY`.

## Implantação

Implante a função AWS Lambda com o código-fonte e as configurações adequadas, como tamanho da memória, tempo limite e gatilhos necessários.

Lembre-se de empacotar todas as dependências do projeto antes de implantar no AWS Lambda.
