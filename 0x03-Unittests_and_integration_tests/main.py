#!/usr/bin/python3
from utils import (
    get_json,
    access_nested_map,
    memoize
)

url = "https://www.swapi.tech/api/people/1"

nested_map = {"a": {"b": 2}}
path = ("a", "b")

print(access_nested_map(nested_map, path))

