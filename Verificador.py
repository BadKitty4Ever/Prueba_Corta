def minusculas(password):
    for char in password:
        if char.islower():
            return True
    return False

def mayusculas(password):
    for char in password:
        if char.isupper():
            return True
    return False

def numeros(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def ocho_o_mas(password):
    for char in password:
        if len(password) > 8:
            return True
    return False