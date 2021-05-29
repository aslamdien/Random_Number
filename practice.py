# CREATE A LOOP
# column style
# for x in range(1, 11):
    # print(x)

# Row style
# for number in range(11):
    # print(number, end = " ")

# Countdown loop
# for numbers in range (100, 0, -2):
    # if numbers == 50:
       #  break
    # print(numbers, end=",")


# Loop through a string
# for x1 in "masimthebe":
    # print(x1)

# Loop thought names
# names = ["Zoe", "Lihle", "Aaliyah", "Masi"]
# for x in names:
    # if x == "Lihle":# To skip Lihle
        # continue # Use continue to skip
    # print(x)

# Nested Loop
#Name = ["Zoe", "Lihle", "Aaliyaah", "Masi"]
#marks = [95, 68, 60, 100]
#for x in range(4):
   # print(Name[x], marks[x])

#FUNCTION
# Adding two number
Num1 = input("Enter First NUmber ")
Num2 = input("Enter Second Number ")
answer = Num1 + Num2
print(answer)

# Def with function Name and parameter
def Addition(x, y):
    answer = x + y
    return answer

print(Addition(7,8))

