import pytest
import requests
import json
from jsonschema import validate


def test_1(base_url):

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
    }

    res = requests.get(base_url + "posts")
    data = res._content.decode('utf-8')
    content = json.loads(data)
    assert res.status_code == 200
    assert type(content) == list

    for item in content:
        validate(item, schema)


@pytest.mark.parametrize("item_id", ["1", "5", "10", "15"])
def test_2(base_url, item_id):
    res = requests.get(base_url + f"posts/{item_id}" )
    data = res._content.decode('utf-8')
    content = json.loads(data)
    assert res.status_code == 200
    assert type(content) == dict
    assert content["id"] == int(item_id)


@pytest.mark.parametrize("post_id", [1, 4, 7])
def test_3(base_url, post_id):
    res = requests.get(base_url + f"comments?postId={str(post_id)}")
    data = res._content.decode('utf-8')
    content = json.loads(data)
    assert res.status_code == 200
    assert type(content) == list
    for item in content:
        assert item["postId"] == post_id


def test_4(base_url):
    message = {
        "headers": {
            'Content-type': 'application/json; charset=UTF-8',
        },
        "body": {
            "title": 'foo',
            "body": 'bar',
            "userId": 1,
        }
    }
    res = requests.post(base_url + "posts", message)
    assert res.status_code == 201


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_5(base_url, post_id):
    new_title = f"foo{str(post_id)}"
    message = {
        "headers": {
            'Content-type': 'application/json; charset=UTF-8',
        },
        "body": {
            "title": new_title,
        }
    }
    res = requests.patch(base_url + f"posts/{str(post_id)}", message)
    assert res.status_code == 200



