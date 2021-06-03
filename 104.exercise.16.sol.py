def common_finder(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,5,8,2], [1,7,2,6]))
