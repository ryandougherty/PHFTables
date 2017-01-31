import constants
import construction

class WalkerColbourn_JMC07_Thm215(construction.Construction):
	def run(self):
		for s in range(1, int((constants.limits.t_limit-1)/2+1)):
			for m in range(2, constants.limits.k_limit):
				if m*s+m <= constants.limits.k_limit and m*s+1 <= constants.limits.v_limit and 2*s+1 <= constants.limits.t_limit:
					other_values = list(range(m*s))
					array = []
					insertion = [(m*s+1)-1]*m # for 0 indexing
					for row in range(s+1):
						index_to_insert = row*m
						other_copied = other_values[:]
						final = other_copied[:index_to_insert] + insertion + other_copied[index_to_insert:]
						array.append(final)

					to_write = self.reference() + '\n'
					for row in array:
						to_write += ' '.join([str(elem) for elem in row])
						to_write += '\n'

					with open(constants.formatPHFfilename(s+1, m*s+m, m*s+1, 2*s+1), 'w') as f:
						f.write(to_write)

	def reference(self):
		return 'Perfect Hash Families: Constructions and Existence (Walker-Colbourn, 2007)'

if __name__ == '__main__':
	b = WalkerColbourn_JMC07_Thm215()
	b.run()