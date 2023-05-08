
import importlib

class_name = (input("Enter the class name: ")).capitalize()
module_name = (input("Enter the module name: ")).lower()

module = importlib.import_module(module_name)
class_ = getattr(module, class_name)

# module = importlib.import_module("mymath")

# l = []
# l.append(int(input("Enter the noss : "))

lst = list(map(int,input("Type number with space : ").split()))
choice = int(input("Enter your choice: "))

if choice == 1:
    add = class_(lst)
    print("Sum: ", add.doAdd())
elif choice == 2:
    sub = class_(lst)
    print("Difference: ", sub.doSubtract())
elif choice == 3:
    multiply = class_(lst)
    print("Product: ", multiply.doMultiply())
elif choice == 4:
    divide = class_(lst)
    print("Quotient: ", divide.doDivide())
