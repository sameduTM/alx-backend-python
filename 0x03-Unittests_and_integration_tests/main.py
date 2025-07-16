#!/usr/bin/python3
from utils import (
    get_json,
    access_nested_map,
    memoize
)

url = "https://www.swapi.tech/api/people/1"

test_url="http://example.com"
test_payload={"payload": True}


print(get_json(url))

