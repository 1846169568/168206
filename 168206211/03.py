#¿ìËÙÅÅĞò
import random
def quicksort(array):
	if len(array)<2:
		return array
	else:
		pivot=array[0]
		less=[i for i in array[1:] if i<=pivot]
		greater=[i for i in array[1:] if i>pivot]
		return quicksort(less)+[pivot]+quicksort(greater)
s=random.sample(range(10),10)
print(s)
print(quicksort(s))