c=2021
f=int(input("Enter the final year"))
print("The future Leap years are:")
for x in range(c,f+1):
    if(x%4==0 and x%100!=0 or x%400==0):
        print(x)