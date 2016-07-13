from dials.array_family import flex

arr1 = flex.double(flex.grid(1, 2, 4),3)

print arr1.as_numpy_array(), "\n_____\n"

arr1.reshape(flex.grid(4,2))

print arr1.as_numpy_array()
