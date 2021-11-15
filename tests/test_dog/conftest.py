import pytest
import requests
import json


@pytest.fixture(scope="session")
def base_url(request):
    return "https://dog.ceo/api/"


@pytest.fixture()
def subbreeds_fixture(base_url, request):
    breed = "hound"
    target = base_url + f"breed/{breed}/list"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    message = json.loads(data)
    subbreeds = []
    for item in message["message"]:
        subbreeds.append(item)
    return {"breed": breed, "subbreeds": subbreeds}




