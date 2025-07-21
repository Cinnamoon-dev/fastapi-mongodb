# FastAPI MongoDB
É um simples CRUD para cadastrar usuários, utilizando a linguagem de programação Python, o framework FastAPI e MongoDB como banco de dados. 

## Bibliotecas
- FastAPI
- Motor (MongoDB "ORM")
- Pytest

## Como rodar
1. Crie os arquivos `.api.env` e `.db.env`
2. Coloque dentro de `.api.env` `MONGO_CLIENT=mongodb://mongo:27017`
3. Rode os comandos
```bash
docker compose -f "compose.yaml" up --build -d // Builda e roda a aplicação
docker compose -f "compose.yaml" down -t 1 // Derruba os containers
```
4. Acesse na url `localhost:8000/docs`

## Como testar a aplicação
  ```bash
  docker compose -f "compose.test.yaml" up --build -d
  docker exec -i api pytest // comando que executa os testes
  docker compose -f "compose.test.yaml" down --timeout 1
  ```

## Como o CI/CD funciona
<hr>

### Pipeline de Testes
#### Event Trigger
Toda vez que houver um push para a branch `main`.

#### Jobs
Contém apenas um job, que é o que executa os testes.

#### Steps
Executa os mesmos passos de ["Como testar a aplicação"](#Como-testar-a-aplicação)

<hr>

### Pipeline de build
#### Event Trigger
Toda vez que houver um push para a branch `main`.

#### Steps
1. Realiza o login no DockerHub
2. Faz o setup do QEMU <br>
    2.1. Ele é o virtualizador que o Docker usa para criar e rodar as imagens
3. Faz o setup do Docker Buildx <br>
    3.1. Ele é um plugin para o Docker Build que melhora o processo de build. <br>
    3.2. Traz várias vantagens, como mais performance e builds multi-plataforma.
4. Realiza o build e o push da imagem para o DockerHub

<hr>

### Pipeline de Deploy
#### Event Trigger
Toda vez que o pipeline de build for concluído com sucesso.

#### Jobs
Contém apenas o job do deploy.

#### Steps
1. Contém apenas um step que executa comandos do shell em um pc usando ssh. <br>
    1.1. O script que é executado está em `/scripts/deploy.sh`.
