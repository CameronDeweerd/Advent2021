def getData():
    mylist = []
    with open("input.txt", "r") as f:  # log.txt file has line separated values,
        for i in f.readlines():
            i = i.strip()
            mylist.append(int(i))
    print(mylist)
    return mylist

def part1(mylist):
    count = 0
    for index, x in enumerate(mylist[1:]):
        if x > mylist[index]:
            count += 1
    print(count)

def part2(mylist):
    count = 0
    for index, x in enumerate(mylist[3:]):
        if x > mylist[index]:
            count += 1
    print(count)


if __name__ == '__main__':
    data = getData()
    part1(data)
    part2(data)
