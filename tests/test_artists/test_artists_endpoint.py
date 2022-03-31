from config import APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD
from payload import post_artists_payload_json,post_artists_payload_json_invalid
from lib.utils import build_requests_headers, log_important_details
from lib.artists import Artists
request_headers = build_requests_headers()


def test_get_artists_lim_off_response():
    ######  Get all Artists wit limit and offset details
    response = Artists().get_artists_offset_limit(APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD,
                                           100,1)
    assert response.status_code == 200
    log_important_details(response.headers, response.status_code, response.json())


def test_post_get_artists():
    ###### Post a new artist with Post method
    response = Artists().post_get_artists(APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD, post_artists_payload_json.artists_payload)
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["message"] == "Successfully created a new artist"
    log_important_details(response.headers, response.status_code, response.json())

    ###### Get new artist created above with username
    response = Artists().get_artists_username(APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD, "sidhu")
    assert response.status_code == 200
    responsedata = response.json()
    assert responsedata["artist_name"] == "Sidhu Moosewala"
    assert responsedata["artist_genre"] == "Punjabi"
    assert responsedata["albums_recorded"] == 59
    log_important_details(response.headers, response.status_code, response.json())


def test_post_artists_400_invalid():
    ###### Post a new artist with invalid data
    response = Artists().post_artists(APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD, post_artists_payload_json_invalid.artists_payload_invalid)
    assert response.status_code == 400
    responsedata = response.json()
    assert type(responsedata["message"]) is str
    log_important_details(response.headers, response.status_code, response.json())


def test_get_artists_400_invalid():
    ###### Get method for new invalud artists
    response = Artists().get_artists_username(APP_URL_ARTISTS, ADMIN_USER, ADMIN_PASSWORD, 56253)
    assert response.status_code == 400
    responsedata = response.json()
    assert type(responsedata["message"]) is str
    log_important_details(response.headers, response.status_code, response.json())
