list1 = [] 
for i in range(5):
    n = int(input("Enter number  for list1: "))
    list1.append(n)

list2 = [] 
for i in range(5):
    num = str(input("Enter number  for list2: "))
    list2.append(num)

a = list1 + list2 
print("Combined list:", a)
