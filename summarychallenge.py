print("""Please choose your option from the list below:
1:      Learn Python
2:      Learn Java
3:      Go swimming
4:      Have dinner
5:      Go to bed
0:      Exit""")
# my try... alhamdulillah
choice =1
while choice:
    choice = input()
    if choice=="0": # choice== 0 you have to press 0 twice to exit because input () changed choice to str
        break
    elif choice in "123456":
        print("You chose {}".format(choice))
# code from Tim Buchalka
print("""Please choose your option from the list below:
1:      Learn Python
2:      Learn Java
3:      Go swimming
4:      Have dinner
5:      Go to bed
0:      Exit""")
while True:
    choice = input()
    if choice=="0":  # choice== 0 you have to press 0 twice to exit because choice is str
        break
    elif choice in "123456":
        print("You chose {}".format(choice))