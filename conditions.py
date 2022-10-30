#conditions.py

age = int (input("How old are you?"))

#if age >=16 and age <=65: #The above statement if statement can be replaced using range as below
if age in range(16,66):
    print("May Allah bless you content with your work  ")
else:
    print("Enjoy your free time")

print("_" * 80)
if age <16 and age >65:
    print("Enjoy your free time")
else:
    print("May Allah bless you content with your work  ")