import inPassage
import simple_example
import CityScapes
import Oz
from scheduler import *
import sys

def eval(dancer, pieces, domain, solution):
	problem = Scheduler(dancers, pieces, domain)
	problem.set_initial(pieces, dancers)
	problem.set_slots(actual = solution)
	problem.get_violations()
	score = problem.evaluate()
	print ('This solution has {} violations'.format(len(problem.violations)))
	if problem.violations:
		for v in problem.violations:
			print ("{} cannot attend {}'s piece at {}".format(v[0], v[1].choreographer.name, v[1].slot))
	print ('Score: {}'.format(score))
	return score

if __name__ == '__main__':
	datasets = {
	'Oz' : [Oz.dancers, Oz.pieces, Oz.domain3, Oz.actual],
	'InPassage': [inPassage.dancers, inPassage.pieces, inPassage.domain, inPassage.actual],
	'CityScapes': [CityScapes.dancers, CityScapes.pieces, CityScapes.domain, CityScapes.actual], 
	'simple':[simple_example.dancers, simple_example.pieces,simple_example.domain]
	}

	args = sys.argv[1:]
	show = args[0]
	if show in datasets:
		dancers = datasets[show][0]
		pieces = datasets[show][1]
		domain = datasets[show][2]
		actual = datasets[show][3]
		eval(dancers,pieces, domain, actual)
	else:
		print ('Show not found')