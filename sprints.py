import sys

def MyFunc(myList):
    sum = 0
    count = 0
    maxFloat = sys.float_info.min
    for i in myList:
        if isinstance(i, float)==True:
            if i>maxFloat:
                maxFloat=i
        if isinstance(i, int)==True and i%2==0:
            sum = sum + i
            count = count + 1
    if count>0 and maxFloat>sys.float_info.min:
        return int(sum/count), maxFloat
    elif count==0 and maxFloat>sys.float_info.min:
        return "there are no even integers", maxFloat
    elif count>0 and maxFloat==sys.float_info.min:
        return int(sum/count), "there are no floats"
    elif count==0 and maxFloat==sys.float_info.min:
        return 0