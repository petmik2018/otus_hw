import pytest
import requests
import json


@pytest.fixture(scope="session")
def base_url(request):
    return "https://api.openbrewerydb.org"


@pytest.fixture()
def postal_codes_fixture(base_url, request):
    city = "New York"
    target = base_url + f"/breweries?by_state=new_york"
    response = requests.get(target)
    data = response.content.decode('utf-8')
    items_list = json.loads(data)
    postal_codes = []
    for item in items_list:
        postal_codes.append(item["postal_code"])
    return {"city": city, "postal_codes": postal_codes}