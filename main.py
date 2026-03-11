from verify_numbers import *


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
    
    inventory_dictionary["items_name"].append(input("Item name: "))
    is_ok=False
    while is_ok==False:
        value=input("Item price: ")
        if (verify_floatnumber(value)):
            value1=float(value)
            inventory_dictionary["prices_by_1"].append(value1)
            is_ok=True
        else:
            print("The previous item price is not valid")
    is_ok=False
    while is_ok==False:  
        value=input("Item quantity: ")
        if (verify_intnumber(value)):
            value2=int(value)
            inventory_dictionary["quantitys"].append(value2)
            is_ok=True
        else:
            print("The previous item quantity is not valid")
    total=value1*value2
    total_to_pay=total_to_pay+total            
    inventory_dictionary["total_price"].append(total)            
    keep=input("Do you want to keep adding items YES/NO: ").lower()
    if keep=="no":
        keep_buying=False
print("")
print("------- Report -------")
print("")
for i in range(len(inventory_dictionary["items_name"])):
    print(f"Product: {inventory_dictionary["items_name"][i]}")
    print(f"Unit Price: {inventory_dictionary["prices_by_1"][i]}")
    print(f"Quantity: {inventory_dictionary["quantitys"][i]}")
    #print(f"Total: {inventory_dictionary["total_price"][i]}")
    print("")

print(f"Total Earned : {total_to_pay}")   