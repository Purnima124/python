sailery=int(input("enter the sailery :"))
if sailery<=10000:
    print("watchman ki sailery") 
elif sailery>10000 and sailery<=25000:
    print("teacher ki sailery")
elif sailery>25000 and sailery<=30000:
    print("prisimpal ki sailery")
else:
    print("this amount is not among these")