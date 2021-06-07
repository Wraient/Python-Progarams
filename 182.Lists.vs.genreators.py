import time

t1 = time.time()
l = [i**2 for i in range(10000000)] # 10 million
print(f"Lists took {round(time.time()-t1,2)}")

t2 = time.time()
g = (i**2 for i in range(100000000000000000000000))
print(f"Genrators took {round(time.time()-t2,2)} seconds")

