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
        self.__name = name
        self.__price = price
        self.quantity = quantity


        # Actions to Execute
        Item.all.append(self)

    @property
    # Property Decorator  = Read-Only Attribute
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    


    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def apply_dicsount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    def calculate_total_price(self):
        return self.__price * self.quantity
    

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

    # To Send An Email we create different methods as per Functipnality , Will Showcase Abstraction
    def __connect(self,smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Testing abstraction in EMAIL Example
        We use "def __MethodName()" instead of "def MethodName" to abstarct this
        method from Users , User Cannot Directly Instantiate it and Make it accessible from Method only  
        We have {self.name} and {self.quantity} parameters
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect('SMTP_SERVER')
        self.__prepare_body()
        self.__send()