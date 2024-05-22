import sys

#list comprehension
sequence =[i for i in range(1,1000)]

print(sys.getsizeof(sequence))


range_sequence = range(1,1000)

print(sys.getsizeof(range_sequence))