

def add_to_inventory(value,inventory):
    inventory.append(value)
    
def print_inventory(inventory):
    for i in range(len(inventory["items_name"])):
        print(f"Product: {inventory["items_name"][i]}")
        print(f"Unit Price: {inventory["prices_by_1"][i]}")
        print(f"Quantity: {inventory["quantitys"][i]}")
        print(f"Total: {inventory["total_price"][i]}")
        print("")
        
def total_pay(value1,value2):
    total=value1*value2
    return total
        