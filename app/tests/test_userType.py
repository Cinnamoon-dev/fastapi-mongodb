import pytest
from fastapi.testclient import TestClient

from main import app

# Casos de teste
# ----------------------------------------------------
# Criar um tipo de usuario valido
# Criar um tipo de usuario com uma string vazia
# Criar um tipo de usuario com um nome ja existente
# ----------------------------------------------------
# Editar um tipo de usuario sem mandar o corpo da requisição, ou com o corpo vazio
# Editar um tipo de usuario para um nome valido
# Editar um tipo de usuario para uma string vazia
# Editar um tipo de usuario para um nome ja existente
# ----------------------------------------------------
# Deletar um tipo de usuario que nao esta sendo usado
# Deletar um tipo de usuario que esta sendo usado
# Deletar um tipo de usuario que nao existe
# ----------------------------------------------------

def create_user_type(name: str) -> str:
    """ Retorna uma string do dict criado, usar em `client.method(content=STRING)`. """
    user_type = {
        "name": name
    }

    return str(user_type).replace("'", "\"")

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_create_valid_user_type(client):
    content = create_user_type("valid_user_type_name")
    response = client.post("/user/type/add", content=content)
    assert response.status_code == 200

def test_create_invalid_user_type(client):
    content = create_user_type("")
    response = client.post("/user/type/add", content=content)
    assert response.status_code == 422

def test_create_repeated_user_type(client):
    content = create_user_type("valid_user_type_name")
    response = client.post("/user/type/add", content=content)
    assert response.status_code == 422

def test_edit_valid_user_type(client):
    content = create_user_type("valid_user_type_name_2")
    existing_user_type = client.get("/user/type/view/name/valid_user_type_name").json()
    response = client.put(f"/user/type/edit/{existing_user_type["data"]["id"]}", content=content)
    assert response.status_code == 200

def test_edit_invalid_user_type(client):
    type_to_edit = create_user_type("type_to_edit")
    client.post("/user/type/add", content=type_to_edit)

    content = create_user_type("")
    existing_user_type = client.get("/user/type/view/name/type_to_edit").json()
    response = client.put(f"/user/type/edit/{existing_user_type["data"]["id"]}", content=content)
    assert response.status_code == 422

def test_edit_repeated_user_type(client):
    mocked_type = create_user_type("mocked_type")
    existing_type = create_user_type("existing_type")

    client.post("/user/type/add", content=mocked_type)
    client.post("/user/type/add", content=existing_type)

    mocked_type_with_id = client.get("/user/type/view/name/mocked_type").json()
    response = client.put(f"/user/type/edit/{mocked_type_with_id["data"]["id"]}", content=existing_type)
    assert response.status_code == 422