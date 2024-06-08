import configuration
import requests
import data


def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)
    return response.json().get("auth_token")

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers={
                             "Content-Type": "application/json",
                             "Authorization": f"Bearer {auth_token}"
                         })

response = post_new_client_kit(data.Kit,data.auth_token)
print(response.status_code)
print(response.json())
