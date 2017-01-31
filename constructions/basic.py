import constants
import construction

class BasicConstruction(construction.Construction):
	def run(self):
		for t in range(2, constants.limits.t_limit):
			for v in range(t, constants.limits.v_limit):
				to_write = self.reference()
				to_write += '\n'
				to_write += ' '.join([str(elem) for elem in list(range(v))])
				with open(constants.formatPHFfilename(1,v,v,t), 'w') as f:
					f.write(to_write)

	def reference(self):
		return '1 Symbol per Row'

if __name__ == '__main__':
	b = BasicConstruction()
	b.run()