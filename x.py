#bubble
arr = [5,3,7,9,8]
n = len(arr)
for i in range(n) :
    for j in range (0,n-i-j) :
        if arr[j] > arr[j+1] :
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

#sqrlist
nums = [1,2,3,4]
num_sqr = [num **2 for num in nums]
print(num_sqr)

#fib
n = int(input("num"))
fib_series =[0,1]
for i in range (0,n) :
    next_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(next_fib)
print(fib_series)

#palindrom
def is_palindrom(sequence):
    sequence = sequence.replace("","").lower()
    return sequence == sequence[::-1]
s = input("input word :")
if is_palindrom(s):
    print("palindrom")
else :
    print("not a palindrom")
