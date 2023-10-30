from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        # Call to Super Function to have access to all attributes / Methods
        super().__init__(name, price, quantity)

      