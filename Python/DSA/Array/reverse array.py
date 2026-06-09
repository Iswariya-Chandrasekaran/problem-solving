arr=[3,5,78,90,23,23]

reverse_arr=arr[::-1]
print(reverse_arr)

print(arr.reverse())

""""
How Slicing Works in Python
The general syntax for slicing is sequence[start:stop:step]. 
start: The beginning index (inclusive). If omitted, it defaults to the beginning of the
 sequence (index 0) when the step is positive, or the end of the sequence when the step is negative.
stop: The ending index (exclusive). If omitted, it defaults to the end of the sequence
 when the step is positive, or the beginning of the sequence when the step is negative.
step: The interval between elements. The default is 1. A negative step, like -1, 
means the sequence is traversed in reverse order.

"""