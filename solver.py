from scheduler import *
import helper
import random, sys, math


def solve(dancers, pieces, domain, algorithm, randomness = False):
	problem = Scheduler(dancers, pieces, domain)
	problem.set_initial(pieces, dancers)
	invalid_pieces = helper.check_empty(problem)
	if invalid_pieces:
		relax_constraints_before(problem, invalid_pieces)
		print ("num of violations", len(problem.violations))


	algo = {
	'naive': problem.set_times,
	'heuristic': problem.heuristic,
	'DFS': problem.DFS,
	'random': problem.random_SA
	}
	

	output = helper.eval(algo[algorithm], pieces)
	while not output:
		problem.relax_constraints_after(randomness)
		output = helper.eval(algo[algorithm], pieces)

	problem.set_slots()
	score = problem.evaluate()

	for p in pieces:
		if p.slot:
			print ("the assigned time for {} piece is {}".format(p.choreographer.name, p.slot))
		else:
			print ("Unable to assign time slot to {} rehearsal".format(p.choreographer.name))

	for d in dancers:
		if d.times:
			print ("{} has these times scheduled: {}".format(d.name, d.times))

	print ('This solution has {} violations'.format(len(problem.violations)))
	if problem.violations:
		for v in problem.violations:
			print ("{} cannot attend {}'s piece at {}".format(v[0], v[1].choreographer.name, v[1].slot))
	print ('Score: {}'.format(score))

if __name__ == '__main__':
	datasets = {
	'Oz' : [Oz.dancers, Oz.pieces, Oz.domain3],
	'InPassage': [inPassage.dancers, inPassage.pieces, inPassage.domain],
	'CityScapes': [CityScapes.dancers, CityScapes.pieces, CityScapes.domain], 
	'simple':[simple_example.dancers, simple_example.pieces,simple_example.domain]
	}

	args = sys.argv[1:]
	show = args[0]
	algorithm = args[1]
	if show in datasets:
		dancers = datasets[show][0]
		pieces = datasets[show][1]
		domain = datasets[show][2]
		solve(dancers,pieces, domain, algorithm)
	else:
		print ('Show not found')