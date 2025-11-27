import json
from json_to_toon.converter import to_toon, to_json

def test_round_trip_simple():
    data = {"title": "My Config", "owner": {"name": "Admin", "id": 55}}
    toon = to_toon(data)
    assert "title = \"My Config\"" in toon
    back = json.loads(to_json(toon))
    assert back == data

def test_invalid_toon_raises():
    bad = "title = [unquoted]"
    import pytest
    with pytest.raises(Exception):
        to_json(bad)
