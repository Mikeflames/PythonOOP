import csv

class Item:
    # Class Attributes
    pay_rate = 0.8
    all = []

    # This is Magic Method for Initializing The Object of Class Item
    def __init__(self,name:str,price:float,quantity=0):
        # Run Validations to recieved arguments
        assert price >= 0 , f"Price must be greater than zero, it is {price} "
        assert quantity >= 0 , f"Quantity must be greater than zero, it is {quantity} "
        
        # print(f"An Instance cresated of : {name} with price : {price} and quantity : {quantity}")
        # Assign to Self Objects , these are Instance attributes -> name , price , quantity
        self.name = name
        self.price = price
        self.quantity = quantity


        # Actions to Execute
        Item.all.append(self)

    def apply_dicsount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Count out the Float that are point zero
        if isinstance(num,float):  #isinstace inbuilt function.
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False





    def __repr__(self):
        # return f"Item('{self.name},{self.price},{self.quantity})"
        return f"{self.__class__.__name__}('{self.name},{self.price},{self.quantity})"


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# item4.pay_rate = 0.5


# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7.8))

# for instance in Item.all:
#     print(instance.name)

# item3.has_numpad = False    # Additional Flag information can be associated with Object outside Class

# print(item1.calculate_total_price())
# print(Item.__dict__) # All the attributes for class Level
# print(item1.__dict__) # All the attributes for Instance Level

# item1.apply_dicsount()
# item4.apply_dicsount()
# print(item4.price)


# ans = item1.calculate_total_price(item1.price, item1.quantity)
# print(ans)
# print(type(item1))
# print(type(item1.price))
# print(type(item1.quantity))
# print(type(item1.name))
# random_str = "aaa"
# print(random_str.upper())


# Inheritance from Class Item , Phone class is Child Class
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


phone1 = Phone("Samsung",500,10,2)

print(Item.all)
print(Phone.all)
