import json
import os
from pathlib import Path


def load_test_data(file_name):
    base = Path(__file__).resolve().parent
    file_path = base.parent / "test_data" / file_name

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
