from Items import Items
from Transactions import Transactions

class Vendo:
    def __init__(self, name: str = "Water Refilling Vendo"):
        self.name = name
        self.inventory = {
            "500 mL Bottle": Items("500 mL Bottle", 10.0),
            "1 Liter Bottle": Items("1 Liter Bottle", 15.0),
            "5 Liter Bottle": Items("5 Liter Bottle", 40.0)
        }

    def getContainerNames(self):
        return list(self.inventory.keys())

    def getContainer(self, name: str) -> Items:
        return self.inventory[name]
    
    def processTransactions(self, item_name: str, payment: float):
        container_name = self.getContainer(item_name)
        return Transactions(container_name, payment)
