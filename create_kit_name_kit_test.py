import sender_stand_request
import data

def positive_assert(kit):
    auth_token = sender_stand_request.post_new_user(data.new_user)
    response = sender_stand_request.post_new_client_kit(kit, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit["name"]

def negative_assert(kit):
    auth_token = sender_stand_request.post_new_user(data.new_user)
    response = sender_stand_request.post_new_client_kit(kit, auth_token)
    assert response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_create_kit_with_511_characters_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_create_kit_with_0_characters_in_name_get_unsuccessful_response():
    negative_assert(data.kit_body_3)

def test_create_kit_with_512_characters_in_name_get_unsuccessful_response():
    negative_assert(data.kit_body_4)

def test_create_kit_with_special_characters_in_name_get_success_response():
    positive_assert(data.kit_body_5)

def test_create_kit_with_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_6)

def test_create_kit_with_numbers_in_name_get_success_response():
    positive_assert(data.kit_body_7)

def test_create_kit_without_name_parameter_get_unsuccessful_response():
    negative_assert(data.kit_body_8)

def test_create_kit_with_numeric_name_get_unsuccessful_response():
    negative_assert(data.kit_body_9)