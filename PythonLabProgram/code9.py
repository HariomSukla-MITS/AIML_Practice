with open("sample.txt", "w") as file:
    file.write("Hello Python Programming")
uppercase = 0
lowercase = 0

with open("sample.txt", "r") as file:
    text = file.read()

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

print("Uppercase Characters:", uppercase)
print("Lowercase Characters:", lowercase)