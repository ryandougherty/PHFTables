import sys
sys.path.insert(0, '../')

import constants

for t in range(2, constants.t_limit):
	for v in range(t, constants.v_limit):
		to_write = ' '.join([str(elem) for elem in list(range(v))])
		with open(constants.formatPHFfilename(1,v,v,t), 'w') as f:
			f.write(to_write)