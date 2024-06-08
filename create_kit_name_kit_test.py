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

def test_case_1():
    positive_assert(data.kit_body_1)

def test_case_2():
    positive_assert(data.kit_body_2)

def test_case_3():
    negative_assert(data.kit_body_3)

def test_case_4():
    negative_assert(data.kit_body_4)

def test_case_5():
    positive_assert(data.kit_body_5)

def test_case_6():
    positive_assert(data.kit_body_6)

def test_case_7():
    positive_assert(data.kit_body_7)

def test_case_8():
    negative_assert(data.kit_body_8)

def test_case_9():
    negative_assert(data.kit_body_9)