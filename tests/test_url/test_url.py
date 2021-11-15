import pytest
import requests


def test_1(my_url, status_code):
    res = requests.get(my_url)
    res_code = res.status_code
    assert res_code == int(status_code)




