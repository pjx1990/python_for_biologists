import time 
start = time.time() 

# print the sum of the first million cube numbers
x = 0 
for i in range(1000000): 
    x = x + i ** 3 
print(x) 
 
end = time.time() 
print(end - start)