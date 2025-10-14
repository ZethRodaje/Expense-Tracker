from dataclasses import dataclass

# Expense model (represents one record)
@dataclass
class Expense:
    id: int | None
    title: str
    amount: float
    date: str
    category: str
    description: str
