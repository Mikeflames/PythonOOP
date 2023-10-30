from item import Item

class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity=0,broken_phones =0):
        # Call to Super Function to have access to all attributes / Methods
        super().__init__(name, price, quantity)

        # Run Validations for Broken Phone
        assert broken_phones >=0 , f"Broken Phones {broken_phones} is not not greater than Zero"

        # Assign to Self Object
        self.broken_phones = broken_phones

        # Actions to Execute
        # Phone.all.append(self) , #Not necessary in Child Class, because super attribute helps us to access 'all' from Parent Class
