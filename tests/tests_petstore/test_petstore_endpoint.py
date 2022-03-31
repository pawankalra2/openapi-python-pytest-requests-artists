from config import APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD
from payload import post_pet_payload_json
from lib.utils import build_requests_headers, log_important_details
from lib.petstore import PetStore
request_headers = build_requests_headers()


def test_post_get_update_del_pet():
    ######  Post Pet details
    response = PetStore().post_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD,
                                           post_pet_payload_json.postPetJson)
    assert response.status_code == 200
    responsedata=response.json()
    petid = responsedata["id"]
    log_important_details(response.headers, response.status_code, response.json())

    ######   Get above pet details
    response = PetStore().get_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, petid)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["name"] =="mydoggiesg"
    log_important_details(response.headers, response.status_code, response.json())

    ######   Update above pet details
    response = PetStore().update_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, petid)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["message"] ==str(petid)
    log_important_details(response.headers, response.status_code, response.json())

    ######   Get above updated pet details
    response = PetStore().get_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, petid)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["name"] =="mydoggiesgupdated"
    assert responsedata["status"] =="not available"
    assert responsedata["category"]["name"] == "mydoggiesg"
    log_important_details(response.headers, response.status_code, response.json())

    ######   Delete above updated pet details
    response = PetStore().delete_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, petid)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["message"] ==str(petid)
    log_important_details(response.headers, response.status_code, response.json())


def test_404_get_pet_not_found():
    ######   Get details of incorrect petid
    response = PetStore().get_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, 565656556)
    assert response.status_code == 404
    responsedata = response.json()
    assert responsedata["message"] =="Pet not found"
    assert type(responsedata["message"]) is str
    log_important_details(response.headers, response.status_code, response.json())


def test_405_get_pet_invalid_id():
    ######   Get details of invalid petid
    response = PetStore().get_pet_details(APP_URL_PETSSTORE, ADMIN_USER, ADMIN_PASSWORD, "")
    assert response.status_code == 405
    log_important_details(response.headers, response.status_code, response.json())
