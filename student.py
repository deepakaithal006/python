dict={}
new_entries=int(input("enter the number of entries"))
for i in range(new_entries):
    name=input("enter the name")
    roll_no=int(input("enter the roll number"))
    dict[name]=roll_no
print(dict)
