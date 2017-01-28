import sys
sys.path.insert(0, '../')

import constants

for s in range(1, int((constants.t_limit-1)/2+1)):
	for m in range(2, constants.k_limit):
		if m*s+m <= constants.k_limit and m*s+1 <= constants.v_limit and 2*s+1 <= constants.t_limit:

			other_values = list(range(m*s))
			array = []
			insertion = [(m*s+1)-1]*m # for 0 indexing
			for row in range(s+1):
				index_to_insert = row*m
				other_copied = other_values[:]
				final = other_copied[:index_to_insert] + insertion + other_copied[index_to_insert:]
				array.append(final)

			to_write = ''
			for row in array:
				to_write += ' '.join([str(elem) for elem in row])
				to_write += '\n'

			with open(constants.formatPHFfilename(s+1, m*s+m, m*s+1, 2*s+1), 'w') as f:
				f.write(to_write)