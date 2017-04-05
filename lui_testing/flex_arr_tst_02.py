from dials.array_family import flex
cpied = '''
flex_2d_data = img_flex.as_double()
flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
'''

arr1 = flex.double(flex.grid(1, 3, 4),3)
print arr1.as_numpy_array(), "\n_____\n"

arr2 = flex.double(flex.grid(1, 3, 4),4)
print arr2.as_numpy_array(), "\n_____\n"

arr3 = arr1 + arr2

print arr3.as_numpy_array(), "\n_____\n"

'''
arr1.reshape(flex.grid(4,2))

print arr1.as_numpy_array()
'''