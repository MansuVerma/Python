heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

#find lenght of the list
print("The lenght of the list is",len(heroes))

#Add 'black panther' at the end of this list.
heroes.append("black panther")
print(heroes)

#add 'black panther' after hulk and remove it from end.
heroes.remove("black panther")
hero = "hulk"
for i in range(len(heroes)):
    if heroes[i]==hero:
        heroes[i+1] = "black panther"

print(heroes)

#change hulk and thor with doctor strange with one line of code.
heroes[1:3] = ["doctor strange"]
print(heroes)

#Sort the heros list in alphabetical order.
heroes.sort()
print(f"The sorted list is: {heroes}")
        