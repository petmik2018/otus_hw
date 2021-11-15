import pytest
import requests
import json
import cerberus
from jsonschema import validate


def test_1(base_url):
    res = requests.get(base_url)
    assert res.status_code == 200


@pytest.mark.parametrize("state", ["ohio", "new_york", "new mexico", "maryland"])
def test_2(base_url, state):
    target = base_url + f"/breweries?by_state={state}"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    items_list = json.loads(data)
    assert response.status_code == 200


@pytest.mark.parametrize("postal", ["ohio", 12345])
def test_3(base_url, postal):
    target = base_url + f"/breweries?by_postal={postal}"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    items_list = json.loads(data)
    assert response.status_code == 200
    assert items_list == []


def test_4(base_url, postal_codes_fixture):
    for index in postal_codes_fixture["postal_codes"]:
        target = base_url + f"/breweries?by_postal={index}"
        response = requests.get(target)
        data = response.content.decode('utf-8')
        items_list = json.loads(data)
        for item in items_list:
            if item["state"] != postal_codes_fixture["city"]:
                raise AssertionError
    assert True


def test_5(base_url):
    target = base_url + f"/breweries?by_type=micro"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    items_list = json.loads(data)

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "country": {"type": "string"}
        },
        "required": ["id", "name"]
    }

    for item in items_list:
        validate(item, schema)

    # v = cerberus.Validator()
    assert response.status_code == 200
    # assert v.validate(item, schema)

