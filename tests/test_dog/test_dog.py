import pytest
import requests
import json
import re


def test_1(base_url):
    target = base_url + f"breeds/list/all"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    message = json.loads(data)
    assert base_url =="https://dog.ceo/api/"
    assert response.status_code == 200
    assert type(message) == dict
    assert type(message["message"]) == dict


def test_2(base_url):
    target = base_url + f"breeds/image/random"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    message = json.loads(data)

    assert response.status_code == 200
    assert type(message) == dict
    assert message["message"][-4:] == ".jpg"


@pytest.mark.parametrize("breed", ["bouvier", "dalmatian", "husky", "ovcharka"])
def test_3(base_url, breed):
    target = base_url + f"breed/{breed}/images"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    message = json.loads(data)

    assert response.status_code == 200
    assert type(message) == dict
    assert type(message["message"]) == list
    assert all([item[-4:] == ".jpg" for item in message["message"]])


def test_4(base_url, subbreeds_fixture):
    breed = subbreeds_fixture["breed"]
    for item in subbreeds_fixture["subbreeds"]:
        target = base_url + f"breed/{breed}/{item}/images"
        response = requests.get(target)
        data = response.content.decode('utf-8')
        message = json.loads(data)
        assert response.status_code == 200
        assert type(message["message"]) == list
        for elem in message["message"]:
            assert elem[-4:] in [".jpg",  ".JPG", "jpeg"]



@pytest.fixture
def my_subs(base_url, request):
    breed = request.param
    target = base_url + f"breed/{breed}/list"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    message = json.loads(data)
    subbreeds = []
    for item in message["message"]:
        subbreeds.append(item)
    return {"breed": breed, "subbreeds": subbreeds}


@pytest.mark.parametrize("my_subs", ["bulldog", "mastiff"], indirect=True)
def test_5(base_url, my_subs):
    breed = my_subs["breed"]
    for item in my_subs["subbreeds"]:
        target = base_url + f"breed/{breed}/{item}/images"
        response = requests.get(target)
        data = response.content.decode('utf-8')
        message = json.loads(data)
        assert response.status_code == 200
        assert type(message["message"]) == list
        for elem in message["message"]:
            assert elem[-4:] in [".jpg",  ".JPG", "jpeg"]



