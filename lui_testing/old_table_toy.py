from dials.array_family import flex

working_code = '''
# Create a table with 2 columns and 10 rows
table = flex.reflection_table()
table['col1'] = flex.int(10)
table['col2'] = flex.double(10)
assert(table.nrows() == 10)
assert(table.ncols() == 2)
print 'OK'
'''
#not_working_code = '''
ref_table = flex.reflection_table()
ref_table['col1'] = flex.int(5)
ref_table['col2'] = flex.double(5)

row = { 'col1' : 10 }
ref_table.append(row)
#'''

example_from_other_code = '''
for row in table.rows():
  h = row['miller_index']
  i_c = row['intensity.cor.value']
  i_r = row['intensity.sum.value']
  i_c_var = row['intensity.cor.variance']
  i_r_var = row['intensity.sum.variance']
  if( i_c > math.sqrt(i_c_var) and i_r > math.sqrt(i_r_var) ):
    ref_table.append(row)
'''
example_from_test = '''
# Append some rows to the table
    row = { 'col1' : 10 }
    c1 = c1 + [10]
    c2 = c2 + [0]
    c3 = c3 + ['']
    table.append(row)
    assert(table.nrows() == 21)
    assert(table.ncols() == 3)
    assert(table.is_consistent())
    assert(all(a == b for a, b in zip(table['col1'], c1)))
    assert(all(a == b for a, b in zip(table['col2'], c2)))
    assert(all(a == b for a, b in zip(table['col3'], c3)))
    print 'OK'
