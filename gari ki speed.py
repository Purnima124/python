speed=int(input("enter the speed"))
if speed<=70:
    print("ok")
elif speed<=130:
    speed=speed-70
    print(speed//5)
else:
    print("gari dhire chalao") 
    print("licence cancelled")   
