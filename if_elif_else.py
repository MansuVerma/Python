age=int(input("Enter the age: "))

if (age<=18):
    print("This age is not suitable for driving.")
elif (age>18):
    print("This age is suitable for driving.")
elif (age==0):
    print("This is age is not posiible.")
elif (age<0):
    print("Mathematical error.")

print("Code ends...")