




def bubble_sort(x):
    list_len = len(x) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,list_len):
            if x[i] > x[i+1]:
                sorted = False
                x[i],x[i+1] = x[i+1],x[i]

    return x

list_ = [5,3,1,2,4]
print(bubble_sort(list_))























