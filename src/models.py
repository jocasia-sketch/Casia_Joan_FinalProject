"""
models.py

Contains the Expense class.
"""

class Expense:
    """Represents a single expense record."""

    def __init__(self, category, amount, description, date):
        self.category = category
        self.amount = amount
        self.description = description
        self.date = date

    def to_dict(self):
        """Convert object to dictionary."""

        return {
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        """Create Expense object from dictionary."""

        return cls(
            data["category"],
            data["amount"],
            data["description"],
            data["date"]
        )