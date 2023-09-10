"""The function returns True if string is in JSON format, False otherwise."""

import json


def is_correct_json(string: str) -> bool:
    try:
        json_data = string
        data = json.loads(json_data)
        return True
    except ValueError:
        return False
