"""ChatBot project"""
# 1-st stage: greeting
print("Hello! My name is VetaBot.")
print("I was created in 2023.")
# 2-nd stage: name reminder
print("Please, remind me your name.")
name = input("> ")
print(f"What a great name you have, {name}!")
# 3-rd stage: guessing age
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
# 4-th stage: counting numbers
print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))
for i in range(number+1):
    print(f"{i} !")
# 5-th stage: asking a question
print("Let's test your programming knowledge.")
print("What are the primary types of loops in Python?")
print("1. if and else")
print("2. for and while")
print("3. try and except")
print("4. import and from")
while True:
    user_answer = int(input("> "))
    if user_answer == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
