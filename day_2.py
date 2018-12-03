data = open('input_2.txt')
data = data.read()
data = data.split('\n')
count_two = 0
count_three = 0
####### Part 1 ############
for box in data:
    diction = {}
    pair = False
    triple = False
    for character in box:
        if character in diction.iterkeys():
            diction[character] += 1
        else:
            diction[character] = 1
    for val,num in diction.items():
        if num == 2 and not pair:
            count_two += 1
            pair = True
        if num == 3 and not triple:
            count_three += 1
            triple = True

print count_two*count_three

############## Part 2 ##################3
for box in data:
    


