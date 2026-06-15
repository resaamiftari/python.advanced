import numpy as np

arary_2D=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print(arary_2D)

elementi=arary_2D[0][2]
print(elementi)

elementi=arary_2D[1][2]
print(elementi)

#dimensioni
dimension=arary_2D.ndim
print(dimension)

#tipi
shape=arary_2D.shape
print(shape)

#size
madhesia=arary_2D.size
print(madhesia)

sub_array=arary_2D[:2,:2]
print(sub_array)