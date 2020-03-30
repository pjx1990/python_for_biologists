import psutil, os 
 
def print_mem(): 
    process = psutil.Process(os.getpid()) 
    mem = process.memory_info().rss / 1000 
    print("Used this much memory: " + str(mem)) 
 
size = 1000000 
 
s = set(range(size))
target = size/2 
print_mem()
 
def number_in_set(): 
    return target in s