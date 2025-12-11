import requests
import pytest
from utils.logger import logger

@pytest.mark.skip(reason="Solo para pruebas de API")
#Obtener usuarios de la API
def test_get_users(url_base,header_request):
    response = requests.get(f"{url_base}/2", headers=header_request)
    logger.info("Realizando peticion GET para obtener usuario con ID 2")
    #Validacion de status code y contenido
    logger.info("Validando el codigo de estado de la respuesta GET")
    assert response.status_code == 200,logger.error("-----Error al obtener el usuario")
    
    data = response.json()
    logger.info("Validando el ID del usuario obtenido")
    assert data["data"]["id"] == 2,logger.error("-----El ID del usuario no coincide")
    
@pytest.mark.skip(reason="Solo para pruebas de API")
#Crear un nuevo usuario
def test_create_user(url_base,header_request):
    payload = {
        "name": "Damian",
        "job": "Tester Auto"
    }
    response = requests.post(url_base, json=payload, headers=header_request)
    
    #Validacion de status code y contenido
    logger.info("Realizando peticion POST para crear un nuevo usuario")
    assert response.status_code == 201,logger.error("-----Error al crear el usuario")
    
    data = response.json()
    
    #Validar que los datos enviados son correctos
    logger.info(f"Validando los datos del usuario creado: {data['name']}, {data['job']}")
    assert data["name"] == "Damian",logger.error("-----El nombre del usuario no coincide")
    assert data["job"] == "Tester Auto",logger.error("-----El trabajo del usuario no coincide")
    

@pytest.mark.skip(reason="Solo para pruebas de API")
#Eliminar un usuario
def test_delete_user(url_base,header_request):
    response = requests.delete(f"{url_base}/2", headers=header_request)
    
    #Validacion de status code
    logger.info("Realizando peticion DELETE para eliminar usuario con ID 2")
    assert response.status_code == 204,logger.error("-----Error al eliminar el usuario")
    
    