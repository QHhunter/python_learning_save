rivers = {"Nile":"Egypt","Yangtze River":"China","Amazon":"Brazil"}
for river,country in rivers.items():
    print("The "+river+" run through "+country +".")
for river in rivers.keys():
    print(river)
for river in rivers.values():
    print(river)