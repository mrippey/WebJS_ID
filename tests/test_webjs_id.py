import pytest
from webjs_id import fetch_api_data
import requests 
import os 


PUBWWW_API_KEY = os.environ.get("PUB_WWW_API_KEY")


def test_pubwww_api_200():
    response = requests.get('https://publicwww.com/eval/"eval"+filetype:js/?export=csvu' + PUBWWW_API_KEY)
    assert response.status_code == 200


def test_read_json():
    with pytest.raises(FileNotFoundError) as err:
        fetch_api_data(jfile='/path/to/invalid.json')
    assert str(err.value) == "[Errno 2] No such file or directory: '/path/to/invalid.json'"
