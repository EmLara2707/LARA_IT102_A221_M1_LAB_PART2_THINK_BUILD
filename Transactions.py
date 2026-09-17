from Items import Items

class Transactions:
    def __init__ (self, item: Items, payment: float):
        self.item = item
        self.payment = payment

    def noChange(self) -> bool:
        return self.payment >= self.item.price

    def change(self) -> float:
        return self.payment - self.item.price 

    def change_breakdown(self) -> dict:
        remaining = int(self.change())
        denominations = [20, 10, 5, 1]
        breakdown = {}
        for d in denominations:
            breakdown[d] = remaining // d
            remaining %= d
        return breakdown