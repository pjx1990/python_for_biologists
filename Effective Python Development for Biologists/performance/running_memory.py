import psutil, os 
 
def print_mem(): 
    process = psutil.Process(os.getpid()) 
    mem = process.memory_info().rss / 1000 
    print("Used this much memory: " + str(mem)) 
 
print("before creating list one...") 
print_mem() 

r = range(0, 1000000, 2) 

print("after creating list one...") 
print_mem() 

r = [] 

print("after discarding list one...") 
print_mem() 

r = range(1, 1000000, 2) 

print("after creating list two...") 
print_mem() 