import numpy as np

a = np.array([1,2,3,4,5,6]) #1dim
b = np.array([[1,2,4,6],[3,4,9,7]]) #2 dim
c=  np.array([[[1,3],[3,4]],[[4,5],[6,7]]]) #3 dim

#find the dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)

#find the element using indexing
print(f"4th element of 2nd row of array b:{b[1,3]}")

#Array slicing  [start:end:step].
print(b[1:])
print(a[0:4:2])

#Array copy and view

copy_arr = a.copy()
view_arr =  b.view()

print(copy_arr)
print(view_arr)

#array shape 
print(a.shape)

#array reshape
new_arr = a.reshape(3,2)
print(new_arr)

#array iteration

for x in a:
    print(x)

for y in c:
    for z in y:
        for k in z:
            print(k)