import psutil, os 

r = range(1000000)
 
process = psutil.Process(os.getpid()) 
mem = process.memory_info().rss / 1000 
print("Used this much memory: " + str(mem))