from verify_numbers import *
from functions import *

#Dictionary that store the items, prices and the quantitys
inventory_dictionary={
    "items_name":[],
    "prices_by_1":[],
    "quantitys":[],
    "total_price":[]
}

#Boolean that keeps the loop running until the user no longer wants to buy more items
keep_buying=True
#Variable that verifies that the user enters a correct value
is_ok=False


#
total_to_pay=0

print("Welcome to the Store")
while keep_buying:
    
    name=valid_item_name()
    add_to_inventory(name,inventory_dictionary["items_name"])
    is_ok=False
    while is_ok==False:
        value=input("Item price: ")
        if (verify_floatnumber(value)):
            value1=float(value)
            add_to_inventory(value1,inventory_dictionary["prices_by_1"])
            is_ok=True
        else:
            print("The previous item price is not valid")
    is_ok=False
    while is_ok==False:  
        value=input("Item quantity: ")
        if (verify_intnumber(value)):
            value2=int(value)
            add_to_inventory(value2,inventory_dictionary["quantitys"])
            is_ok=True
        else:
            print("The previous item quantity is not valid")
    total=total_pay(value1,value2)
    total_to_pay=total_to_pay+total            
    add_to_inventory(total,inventory_dictionary["total_price"])  
    
    
    keep_buying=valid_option_to_contin()
print("")
print("------- Report -------")
print("")
print_inventory(inventory_dictionary)

print(f"Total Earned : {total_to_pay}")   