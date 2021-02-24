def soma(a,b):
    
    //if b == None:
    //    b = a
    
    if is_number(a) and is_number(b):
        return float(a) + float(b)
    else:
        return None


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
