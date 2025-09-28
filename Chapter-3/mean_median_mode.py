import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
mean = statistics.mean(values)
median = statistics.median(values)
mode = statistics.mode(values)
 
print("The mean is: " + str(mean))
print("The median is: " + str(median))
print("The mode is: " + str(mode))