# Loop through a range of numbers (0 through 4)
for x in range(8):
    print(x)

print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 7):
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
word = "54321"
for letters in word:
    print(letters)
    
print("----------------------------------------")

desired_number = 5
for x in range(10):
    if (x == desired_number):
        break
    print(x)

print("----------------------------------------")

desired_number = 5
for x in range(10):
    if x == 3:
        continue
    print(x)
    
print("----------------------------------------")

# Loop while a condition is being met
run = "y"

while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y'")
