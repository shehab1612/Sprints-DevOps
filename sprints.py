def MyFunc(myList):
    sum = 0
    count = 0
    maxFloat = -1.7976931348623157e+308
    for i in myList:
        if isinstance(i, float)==True:
            if i>maxFloat:
                maxFloat=i
        if isinstance(i, int)==True and i%2==0:
            sum = sum + i
            count = count + 1
    if count>0 and maxFloat>-1.7976931348623157e+308:
        return int(sum/count), maxFloat
    elif count==0 and maxFloat>-1.7976931348623157e+308:
        return "there are no even integers", maxFloat
    elif count>0 and maxFloat==-1.7976931348623157e+308:
        return int(sum/count), "there are no floats"
    elif count==0 and maxFloat==-1.7976931348623157e+308:
        return 0