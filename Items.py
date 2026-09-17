class Items:
    def __init__(self, container, price):
        self.container = container
        self.price = price
    
    def items(self):
        return f"{self.container} | (₱{self.price:.2f})"