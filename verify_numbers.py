def verify_intnumber(number):
    try:
        number=int(number)
        if (number>0):
            return True
    except:
        return False
    

def verify_floatnumber(number):
    try:
        number=float(number)
        if (number>0):
            return True
    except:
        return False