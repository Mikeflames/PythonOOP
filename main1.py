from item import Item
# from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

# Encapsulation Implemented using Getters and Setters
# To restrict Users to not Change Name Directly , So Create Read Only Attributes once after Initialization
item1 = Item("MyItem",750,6)
# item1.apply_increment(0.2)
# item1.price = 100
# print(item1.price)
# print(item1.prepare_body())  -> Error Abstarcted
item1.send_email()
# In Abstarction we dont want to let user use directly use Partial Methods like def connect()
  