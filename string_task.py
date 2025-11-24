import random
user_input = input("Enter a group of letters and symbols separated by (-): ")
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def lowercase(letters):
    return letters.lower()

lowercase_letters = list(map(lowercase, letters))

def change_content(user_input):
    result = ""
    for char in user_input:
        if char.isalpha():
            result += random.choice(letters)
        elif char == "#":
            result += str(random.randint(0,10))
        elif char == "@":
            result += random.choice(lowercase_letters)
        else:
            result += char
    return result

print(change_content(user_input))



