mylist = []
with open("1-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        i = i.strip()
        mylist.append(int(i))
print(mylist)

count = 0
for index, x in enumerate(mylist[1:]):
    if x > mylist[index]:
        count += 1
print(count)

count = 0
for index, x in enumerate(mylist[3:]):
    if x > mylist[index]:
        count += 1
print(count)
