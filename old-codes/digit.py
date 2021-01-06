import unittest
def validate_pin(pin):
    #return true or false
    if len(pin) != 4 and len(pin) != 6 :
        return False
    if pin.isdigit() :
        return True
    return False



pin = "123a"
print(validate_pin(pin))
