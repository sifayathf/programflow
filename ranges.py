for i in range(10,20):  # prints number starting from 10 ending at 19 ie number 20 not including 20
    print(i)

for i in range(10,2):
    print("i is now{}".format(i)) # no output as the end is less than the start

for i in range(0,10,2):
    print("i is now{}".format(i)) # the third argument is step range(start,end,step)

for i in range(10,0,-2):
    print("i is now{}".format(i)) # -ve step output 10,8,6,4,2  starts from 10 descending till 0 in decrements of 2 not including 0

