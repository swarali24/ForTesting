# Python Program to Print Odd Numbers Within a Given Range

starting_range=int(input("enter a starting range"))
ending_range=int(input("enter a ending range"))
for i in range(starting_range, ending_range):
    if (i%2!=0):
        print("is odd", i)