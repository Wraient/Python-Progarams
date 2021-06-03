def common_nums(list1, list2):
    common = []
    for i in list1:
        for m in list2:
            if i == m:
                common.append(i)
            continue
    return common

print(common_nums([1,5,8,2], [1,7,2,6]))
