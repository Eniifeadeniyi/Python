symbols = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_" ,"+", "-", "=", "[" ,"]", "{", "}" ,";","'",":",'"',"|",",",".", "<",">" ,"/","?","~","`"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
password = input("Enter your password: ")
uppercase = password.upper()
lowercase = password.lower()
upper_count = False
lower_count = False
symbol_count = False
number_count = False
for char in uppercase:
    if char in password:
        upper_count = True
        break
for char in lowercase:
    if char in password:
        lower_count = True
        break
for char in symbols:
    if char in password or '?' in password:
      symbol_count = True
      break
for digit in numbers:
    if digit in password:
        number_count = True
        break

def validate(upper_count, lower_count, symbol_count, number_count):
    if upper_count == True and lower_count == False and symbol_count == False and number_count == False and len(password) < 10:
            return "Weak"
    elif upper_count == False and lower_count == True and symbol_count == False and number_count == False and len(password) < 10:
        return "Weak"
    elif upper_count == False and lower_count == False and symbol_count == True and number_count == False and len(password) < 10:
        return "Weak"
    elif upper_count == False and lower_count == False and symbol_count == False and number_count == True and len(password) < 10:
        return "Weak"
    elif upper_count == False and lower_count == False and symbol_count == False and number_count == False and len(password) >= 10:
        return "Weak"
    elif upper_count == True and lower_count == True and symbol_count != True and number_count == False and len(password) < 10:
        return "Medium"
    elif upper_count == True and lower_count == True and symbol_count != True and number_count == True and len(password) < 10:
        return "Medium"
    elif upper_count == True and lower_count == True and symbol_count == True and number_count == True and len(password) >= 10:
        return "Strong"

print(validate(upper_count, lower_count, symbol_count, number_count))