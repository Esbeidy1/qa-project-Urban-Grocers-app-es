import configuration
import requests
import data


def post_new_user(body): #La función 'post_new_user' es para crear usuario y obtener el token de autenticación.
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)
    return response.json().get("auth_token")

def post_new_client_kit(kit_body, auth_token): #la función 'post_new_client_kit' crea kit de cliente con el token de autenticación.
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers={
                             "Content-Type": "application/json",
                             "Authorization": f"Bearer {auth_token}"
                         })


