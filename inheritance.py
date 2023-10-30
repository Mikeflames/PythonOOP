from phone import Phone
# We have Used Child Class here,
# We have Reused Code across Classes Using Inheritance.
item1 = Phone("Samsung",1000,3)
item1.apply_increment(0.2)
print(item1.price)
item1.send_email()

