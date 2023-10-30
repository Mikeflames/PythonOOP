# One Single Entity which you can Use for Multiple Objects
# PolyMorphism and Inhetitance Sometime Comes Together.
# Can be implemented by using Abstract Classs in Python ( interrfaces in other Languages)
from keyboard import Keyboard

item1 = Keyboard("Dell",1000,3)
item1.apply_dicsount()
print(item1.price)