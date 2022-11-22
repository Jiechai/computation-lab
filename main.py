import numpy as np
# median function
def median_filter(input_list, filter_length):
    start = (filter_length -1)//2
    stop = (filter_length -1)//2 + len(input_list)
    input_padding = [0 for _ in range(len(input_list) + filter_length -1)]
    input_padding[start:stop] = input_list

    #print(input_padding)
    i = 0
    while i < len(input_list):
        b = sorted(input_padding[i:i + filter_length])
        #print(b)
        input_list[i] = b[(filter_length - 1)//2]
        i = i + 1

    return input_list

#test function 
def test_filter(input_list, filter_length):
    start = (filter_length -1)//2
    stop = (filter_length -1)//2 + len(input_list)
    input_padding = [0 for _ in range(len(input_list) + filter_length -1)]
    input_padding[start:stop] = input_list

    #print(input_padding)
    i = 0
    while i < len(input_list):
        b = np.median(input_padding[i:i + filter_length])
        #print(b)
        input_list[i] = int(b)
        i = i + 1

    return input_list
#main code 

#a = [4, 2, 2, 4, 5, 7, 3]
a = [9,8,7,5,6,12,9,8,6,4]

filter_length = int(input("please input window length:" ))
while (filter_length - 1)//2 < 1 or (filter_length - 1)%2 != 0:
    filter_length = int(input("please input an odd number(bigger than 3):" ))
a = median_filter(a, filter_length)
print(a)
# test 
b = test_filter(a, filter_length)

print(b)
i = 1
while a[i] != b[i]:
    print('wrong')
    i = i +1
else:
    print('true')
    i = i +1






    




    









