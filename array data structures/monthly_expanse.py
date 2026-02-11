list = [2000,2350,2600,2130,2190]


#find dollars expand in feb
print(f"The more expanse in Feb as compare to Jan is :{list[1]} - {list[0]} = ",list[1] - list[0])

#Total expanse in first quarter.
print(f"The Total expanse in first quarter is ",list[0] + list[1] + list[2])

#Find if expand 2000 dollars in any month
expand = 2000
for i in range(len(list)):
    if list[i] == expand:
        print(f"The month {list[i]} had an expanse of 2000 dollars")
        i+=1

    else:
        print("No expand as such.")

#You return an item taht you bought in a month of april and got a refund of 200dollars . Make a correction to your expanse list base on this.
a = 200
b = list[3] - a
list[3] = b
print(list)