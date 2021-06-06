roll_no = [1,2,3,4]
maths = [100,90,80,70]
science = [90,70,60,50]
english = [100,99,95,85]
percentage = lambda *args : [round(sum(i)/len(args),2) for i in zip(*args)]

# for i in zip(maths, science, english):
#     for j in range(3):
#         percentage.append(round(i[j]/300,2))



print(percentage(maths, science, english))

