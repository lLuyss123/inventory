

def add_to_inventory(value,inventory):
    inventory.append(value)
    
def print_inventory(inventory):
    for i in range(len(inventory["items_name"])):
        print(f"Product: {inventory['items_name'][i]}")
        print(f"Unit Price: {inventory['prices_by_1'][i]}")
        print(f"Quantity: {inventory['quantitys'][i]}")
        print(f"Total: {inventory['total_price'][i]}")
        print("")
        
def total_pay(value1,value2):
    total=value1*value2
    return total


def valid_option_to_contin():
    is_ok=False
    while is_ok==False:
        value=input("Do you want to keep adding items YES/NO: ").lower()
        if value=="no":
            return False
        elif value=="yes":
            return True
        else:
            print("ONLY YES OR NO")
            
def valid_item_name ():
    is_ok=False
    while is_ok==False:
        item_name=input("Item name: ").strip()
        
        if len(item_name)==0:
            print("Item name is not valid")
        else:
            is_ok=True
            return item_name