#Make a benchmark
#Using pythons time module, start a timer on the first line, make the program do many complex
#calculations (e.g multiply all numbers from 0-1mil by 2) and when finished, stop the timer.
#print out the time taken

import time


number = range(1 , 1000000)


start_t = int(round(time.time() * 1000))
print(start_t)
for n in number:
    total = n * 2
    print(total)

stop_t = int(round(time.time() * 1000))
print(stop_t)
total = (stop_t - start_t) // 1000.0

print("the script totally took %s seconds" %(total))

