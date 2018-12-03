indata = open('input_1.txt')
indata = indata.read()
indata = indata.split('\n')
# print (indata)
datasave = []
dataint = 0
founddata =False
####Part 1#########
# for i in indata:
#     datasave += int(i)
# print datasave
####Part 2#########
while not founddata:
    for i in indata:
        datanew = int(i)
        dataint += datanew
        if dataint in datasave:
            print dataint
            founddata=True
            break
        datasave.append(dataint)


