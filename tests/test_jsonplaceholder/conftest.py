import pytest
import requests
import json


@pytest.fixture(scope="session")
def base_url(request):
    return "https://jsonplaceholder.typicode.com/"