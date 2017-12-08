import inPassage
import simple_example
import CityScapes
import Oz

import helper
import random, sys, math


class Scheduler:
	def __init__(self, dancers, pieces, domain, violations = []):
		self.dancers = dancers
		self.pieces = pieces
		self.domain = domain
		self.violations = violations

	def set_initial(self, pieces, dancers):
		for p in pieces:
			for d in p.performers:
				#p.times, d.constraint_weights[p] = helper.crossOff(p.times, d.availability)
				p.times, d.constraint_weights[p] = helper.crossOff(p.times, d.availability)
		
	def set_times(self, pieces):
		#iterate through the remaining times in each rehearsal
		#naively assign the first times
		for p in pieces:
			if p.times:
			#set rehearsal time to the first time
				p.slot = p.times[0]
			for x in pieces:
				if p.slot in x.times:
					x.times.remove(p.slot)
		return True
	
	# USING HEURISTIC
	def heuristic(self, pieces):
		ordered = helper.order(pieces)
		names = [x.choreographer.name for x in ordered]
		print ("the order of assignments is {}".format(names))
		while ordered:
			MRV = ordered[0]
			counts = helper.time_counts(ordered)
			values = [(x, counts[x]) for x in MRV.times]
			ordered = helper.order(ordered[1:])
			while len(values) != 0:
				#find the least constraining value
				LCV = min(values, key=lambda x: x[1])
				MRV.slot = LCV[0]
				if helper.check(ordered, MRV.slot):
					#print ('{} is assigned to {}'.format(MRV.choreographer.name, MRV.slot))
					for x in ordered:
						if MRV.slot in x.times:
							x.remove_time(MRV.slot)
					#go to assigning the next piece
					break
				else:
					#go to the next least constraining value
					MRV.slot = None
					values.remove(LCV)
					#if no more values remain
					if not values:
						print ("Unable to assign time slot to {} rehearsal".format(MRV.choreographer.name))
						return False
		return True


	def DFS(self, pieces):
		
		def makeTree(pieces):

			class Node:
			    def __init__(self, name, time, successors = None, path = []):
			        self.name = name
			        self.time = time
			        self.successors = successors
			        self.path = path

			    def add_path(self, old_path, node):
			        self.path = old_path[:]
			        self.path.append(node.time)

			    def add_successors(self, successors):
			        self.successors = successors

			#DO WE EVEN NEED A HEURISITC TO ORDER THE TREE?
			#create start node
			start = Node('start', None)
			current = [start]
			#order the domain 
			ordered = helper.time_counts(pieces)
			number_nodes = 1
			for p in helper.order(pieces):
				successors = []
				times = sorted(p.times, key = lambda x: ordered[x])
				for t in times:
					new_node = Node(p.choreographer, t)
					successors.append(new_node)
				for c in current:
					c.add_successors(successors)
				number_nodes *= len(successors)
				current = successors
			print ('This tree has a total of {} nodes to explore'.format(number_nodes))
			return start


		start_node = makeTree(pieces)
		if not start_node:
			return False
		solutions = []
		sol_scores = []
		#traverse tree
		stack = [start_node]
		while stack:
			#print ('stack', len(stack))
			vertex = stack.pop()
			if vertex.successors:
				for child in vertex.successors:
					#need to a check that the child is not contained in the path before
					if child.time not in vertex.path:
						#update the childs path
						child.add_path(vertex.path, child)
						#add the child to the stack
						stack.append(child)
			#if at the deepest level in tree (no children)
			else:
				solutions.append(vertex.path)
				#self.assign_solution(vertex.path)
				self.set_slots(solution = vertex.path)
				score = self.evaluate()
				sol_scores.append((vertex.path, score))

		if not solutions:
			#for i,s in enumerate(solutions):
				#print ("Solution {}: {}".format(i, s))
			print ('no valid assignment found')
			return False


		#return solutions

		#rate solutions
		
		#print ('sol_scores', [x[1] for x in sol_scores])
		best = max(sol_scores, key=lambda x: x[1])[0]
		#best_set = [x for x in sol_scores if ]
		#print ('sol_scores', [x[1] for x in sol_scores]) ### NEED TO IMPLEMENT THIS
		#print ('best',best)
		#self.assign_solution(best)
		self.set_slots(solution = best)
		return True

	def get_violations(self):
		self.violations = []
		for p in self.pieces:
			for d in p.performers:
				if p.slot not in d.availability:
					self.violations.append((d.name,p))



	def random(self, pieces):

		#reset
		for p in pieces:
			p.times = p.choreographer.availability
		#assign times randomly as start
		ordered = helper.order(pieces)
		for i, p in enumerate(ordered):
			p.slot = random.choice(p.times)
			for x in ordered[i+1:]:
				if p.slot in x.times:
					x.times.remove(p.slot)

		self.set_slots()
		self.get_violations()


		def get_available_times(piece):
			times = piece.choreographer.availability
			for p in pieces:
				if p.slot in times:
					times.remove(p.slot)
			return times

		#change to minimum conflict heuristics

		def assign_to_neighbor(piece):
			neighbor_times = get_available_times(piece)
			if neighbor_times:
				rand = random.choice(neighbor_times)
				piece.slot = rand

		def run(T, schedule):
			accepted = []
			while T > 1:
				current_value = self.evaluate() - len(self.violations)
				rand_piece = random.choice(self.violations)[1]
				old = rand_piece.slot
				assign_to_neighbor(rand_piece)
				self.set_slots()
				self.get_violations()
				print ('violations',len(self.violations))
				new_value = self.evaluate() - len(self.violations)
				delta = new_value - current_value
				if delta >= 0:
					accepted.append(new_value)
				else:
					if random.random() < math.exp(delta / float(T)):
						accepted.append(new_value)
					else:
						rand_piece.slot = old
						self.set_slots()
						self.get_violations()
				T *= schedule
			print (accepted)

		run(10000, 0.95)
		return True



	#def run(T, schedule):








	
	def relax_constraints_after(self, randomness):
	#remove the dancer from the piece with the most dancers
	#remove dancers who are in a lot of pieces
		def get_dancer_count(pieces):
			counts = []
			for p in pieces:
				counts.append((p, len(p.performers)))
			#return counts
			return (max(counts, key = lambda x: x[1]))[0]

		def find_most_constraining(piece):
			#count the overlap between the choreographer's availabiity and the dancer's availabiity
			performer_overlap = []
			for d in piece.performers:
				overlap = list(set(d.availability).intersection(piece.choreographer.availability))
				performer_overlap.append((d, len(overlap)))
			return performer_overlap

		biggest_piece = get_dancer_count(self.pieces)
		if randomness:
			if random.random() > 0.8:
				biggest_piece = random.choice(self.pieces)

		overlap = find_most_constraining(biggest_piece)
		most_constraining_dancer = (min(overlap, key = lambda x: x[1]))[0]
		
		biggest_piece.remove_dancer(most_constraining_dancer)
		self.violations.append((most_constraining_dancer.name, biggest_piece))
		biggest_piece.times = [x for x in biggest_piece.choreographer.availability if x in self.domain]
		self.set_initial(self.pieces, self.dancers)

		#remove the most contraining dancer from the dancer with the most pieces

	def set_slots(self, solution = None):
		if solution: 
			for p, time in zip(self.pieces, solution):
				p.slot = time
		for d in self.dancers:
			d.times = []
			d.pieces = []
			for p in self.pieces:
				if d in p.performers:
					d.times.append(p.slot)
					d.pieces.append(p.choreographer.name)
			#print ('d.times', d.times)
			d.times = sorted(d.times, key = lambda x: (x.split('.')[0], int(x.split('.')[1])))
	#try to maximize evaluation score
	def evaluate(self):
		#nonharvard students have their rehearsals on the same day
		nonharvard_score = 0
		#check for dinner breaks
		dinner_score = 0
		#check for super late rehearsals (11 pm)
		late_score = 0
		#check that rehearsals are clustered together
		cluster_score = 0
		for d in self.dancers:
			if d.role == 'nonharvard':
				days = [x.split('.')[0] for x in d.times]
				if len(set(days)) == 1:
					nonharvard_score -= 3
				#minimize the time difference
			ind_score = 0
			if d.times:
				for i,t in enumerate(d.times[:-1]):
					if t.split('.')[0] == d.times[i+1].split('.')[0]:
						if abs(int(t.split('.')[1]) - int(d.times[i+1].split('.')[1])) < 2:
							ind_score += 1
							#print ('ind', ind_score)
				cluster_score += (ind_score/len(d.times))
			hours = [int(x.split('.')[1]) for x in d.times]
			if not(5 in hours and 6 in hours):
				dinner_score += 1

		times = [int(p.slot.split('.')[1]) for p in self.pieces]
		late = [x for x in times if x > 10]
		if not late:
			late_score += 1
			

		return nonharvard_score + dinner_score + late_score + cluster_score


def check_empty(problem):
	empty_domain = []
	for p in problem.pieces:
		if not p.times:
			empty_domain.append(p)
	return empty_domain


def relax_constraints_before(problem, invalid_pieces):

#remove dancers with very few time slots (indication that they are busy)
	for p in invalid_pieces: 
		#print ('invalid p', p.choreographer.name)
		if p.performers:
			dancer_counts = []
			for dancer in p.performers:
				dancer_counts.append((dancer, len(dancer.availability)))
			#is_empty = check_empty(problem)
			while not p.times:
				busiest_dancer = (min(dancer_counts, key = lambda x: x[1]))
				p.remove_dancer(busiest_dancer[0])
				dancer_counts.remove(busiest_dancer)
				problem.violations.append((busiest_dancer[0].name, p))
				p.times = [x for x in p.choreographer.availability if x in problem.domain]
				#problem = Scheduler(problem.dancers, problem.pieces, problem.violations)
				#print ('len dancers',len(problem.dancers))
				problem.set_initial(problem.pieces, problem.dancers)
		else:
			p.choreographer.availability = problem.domain
			p.times = p.choreographer.availability
			problem.set_initial(problem.pieces, problem.dancers)
		


def solve(dancers, pieces, domain, algorithm, randomness = False):


	#you can curry functoins
	problem = Scheduler(dancers, pieces, domain)
	problem.set_initial(pieces, dancers)
	invalid_pieces = check_empty(problem)
	if invalid_pieces:
		relax_constraints_before(problem, invalid_pieces)
		print ("num of violations", len(problem.violations))


	algo = {
	'naive': problem.set_times,
	'heuristic': problem.heuristic,
	'DFS': problem.DFS,
	'random': problem.random
	}
	def eval(function, *args):
		return (function(*args))

	output = eval(algo[algorithm], pieces)
	while not output:
		problem.relax_constraints_after(randomness)
		output = eval(algo[algorithm], pieces)

	problem.set_slots()
	score = problem.evaluate()

	for p in pieces:
		if p.slot:
			print ("the assigned time for {} piece is {}".format(p.choreographer.name, p.slot))
		else:
			print ("Unable to assign time slot to {} rehearsal".format(p.choreographer.name))

	for d in dancers:
		print ("{} has these times scheduled: {}".format(d.name, d.times))

	print ('This solution has {} violations'.format(len(problem.violations)))
	if problem.violations:
		for v in problem.violations:
			print ("{} cannot attend {}'s piece at {}".format(v[0], v[1].choreographer.name, v[1].slot))
	print ('Score: {}'.format(score))

if __name__ == '__main__':
	datasets = {
	'Oz' : [Oz.dancers, Oz.pieces2, Oz.domain3],
	'InPassage': [inPassage.dancers2, inPassage.pieces2, inPassage.domain],
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

#relax constraints differentlyl
#fix pre relaxing-- !!!!

#changing variables randomly
#get random solution
#define better solution function
#evaluate heuristic
#use simulated annealing to maximize

#implement randomness
