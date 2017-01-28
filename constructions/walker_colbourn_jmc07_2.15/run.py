import sys
sys.path.insert(0, '../')

import constants

for s in range(1, int((constants.t_limit-1)/2+1)):
	for m in range(2, constants.k_limit):
		if m*s+m <= constants.k_limit and m*s+1 <= constants.v_limit and 2*s+1 <= constants.t_limit:
			array = [[0]*(m*s+m)]*(s+1)
			print(array)
			print(m, s, constants.formatPHFfilename(s+1, m*s+m, m*s+1, 2*s+1))