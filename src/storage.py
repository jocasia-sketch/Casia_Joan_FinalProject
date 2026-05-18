"""
storage.py

Handles saving and loading JSON data.
"""

import json
from pathlib import Path
from models import Expense


ROOT_DIR = Path(__file__).resolve().parents[1]
FILE_PATH = ROOT_DIR / "data" / "expenses.json"
FILE_PATH.parent.mkdir(parents=True, exist_ok=True)


def save_expenses(expenses):
    """Save expenses to JSON file."""

    data = [expense.to_dict() for expense in expenses]

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_expenses():
    """Load expenses from JSON file."""

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

            return [Expense.from_dict(item) for item in data]

    except (FileNotFoundError, json.JSONDecodeError):
        return []