#!/usr/bin/python3
from utils import (
    get_json,
    access_nested_map,
    memoize
)

url = "https://www.swapi.tech/api/people/1"

nested_map = {}
path = ("a",)

print(access_nested_map(nested_map, path))

