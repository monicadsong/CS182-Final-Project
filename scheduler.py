import inPassage
import simple_example
import CityScapes
import Oz

import helper
import random, sys, timeit


class Scheduler:
	def __init__(self, dancers, pieces, domain, violations = []):
		#all dancers
		self.dancers = dancers
		self.pieces = pieces
		self.domain = domain
		self.violations = violations

	def set_initial(self, pieces, dancers):
		for p in pieces:
			for d in p.performers:
				p.times = helper.crossOff(p.times, d.availability)
			#print ('the times avail for {} piece are'.format(p.choreographer.name), p.times)

	#set_initial(self.pieces, self.dancers)

	def set_times(self, pieces):
		#iterate through the remaining times in each rehearsal
		#naively assign the first times
		for p in pieces:
			#print ("the times available for {} piece are {}".format(p.choreographer, p.times))
			if p.times:
			#set rehearsal time to the first time
				p.slot = p.times[0]
			for x in pieces:
				if p.slot in x.times:
					x.times.remove(p.slot)
	
	# USING HEURISTIC
	def assign_backtracking(self, pieces):
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
							#if MRV.slot == 'Tues.7':
							#print ('{} remove time'.format(x.choreographer.name), x.times)
							x.remove_time(MRV.slot)
							#print ('remove time after', x.times)
					#ordered = order(ordered[1:])
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

			#create start node
			start = Node('start', None)
			current = [start]
			#order the domain 
			ordered = helper.time_counts(pieces)
			for p in helper.order(pieces):
				#print ("p.choreographer.name", p.choreographer.name)
				#print ("p.times", p.times)
				successors = []
				times = sorted(p.times, key = lambda x: ordered[x])
				for t in times:
					new_node = Node(p.choreographer, t)
					successors.append(new_node)
				for c in current:
					c.add_successors(successors)
				current = successors
			return start

		start_node = makeTree(pieces)
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
				self.assign_solution(vertex.path)
				score = self.evaluate()
				sol_scores.append((vertex.path, score))

		if not solutions:
			#for i,s in enumerate(solutions):
				#print ("Solution {}: {}".format(i, s))
			print ('no valid assignment found')
			return False


		#return solutions

		#rate solutions
		
	
			#print ('score', score)
		#get minimum score solution
		#print ('sol_scores', [x[1] for x in sol_scores])
		best = min(sol_scores, key=lambda x: x[1])[0]
		#best_set = [x for x in sol_scores if ]
		#print ('sol_scores', [x[1] for x in sol_scores])
		#print ('best',best)
		self.assign_solution(best)
		return True

	
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
				#print ('overlap of {}'.format(d.name), overlap)
				performer_overlap.append((d, len(overlap)))
			return performer_overlap

		biggest_piece = get_dancer_count(self.pieces)
		if randomness:
			if random.random() > 0.5:
				biggest_piece = random.choice(self.pieces)

		#print ('biggest_piece', biggest_piece.choreographer.name)
		overlap = find_most_constraining(biggest_piece)
		most_constraining_dancer = (min(overlap, key = lambda x: x[1]))[0]
		
		#print ('most contraining dancer', most_constraining_dancer.name, most_constraining_dancer.availability)
		biggest_piece.remove_dancer(most_constraining_dancer)
		self.violations.append((most_constraining_dancer.name, biggest_piece.choreographer.name))
		biggest_piece.times = [x for x in biggest_piece.choreographer.availability if x in self.domain]
		self.set_initial(self.pieces, self.dancers)

		#remove the most contraining dancer from the dancer with the most pieces

	def assign_solution(self, solution):
		for p, time in zip(self.pieces, solution):
			p.slot = time
		for d in self.dancers:
			d.times = []
			for p in self.pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)
			d.times.sort()

	def set_slots(self):
		for d in self.dancers:
			d.times = []
			d.pieces = []
			for p in self.pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)
					#print ('p.slot', p.slot)
					d.pieces.append(p.choreographer.name)
			#print ('d.times', d.times)
			d.times.sort()

	def evaluate(self):

		#get dancer assignments
		#self.assign_dancer_times(solution)
		#if nonharvard students must travel on two different days
		nonharvard_score = 0
		#check for dinner breaks
		dinner_score = 0
		#check for super late rehearsals (11 pm)
		late_score = 0
		for d in self.dancers:
			if d.role == 'nonharvard':
				days = [x.split('.')[0] for x in d.times]
				if len(set(days)) > 1:
					nonharvard_score += 3
				#minimize the time difference
				for i,t in enumerate(d.times[:-1]):
					if t.split('.')[0] == d.times[i+1].split('.')[0]:
						if abs(int(t.split('.')[1]) - int(d.times[i+1].split('.')[1])) > 2:
							nonharvard_score += 1
			hours = [int(x.split('.')[1]) for x in d.times]
			#print (hours)
			if 5 in hours and 6 in hours:
				#print ('dancer dinner', d.name)
				dinner_score += 2

		times = [int(p.slot.split('.')[1]) for p in self.pieces]
		for t in times:
			if t > 10:
				late_score += 1

		return nonharvard_score + dinner_score + late_score + len(self.violations)




'''
def has_slot(problem):
	no_slots = []
	for p in problem.pieces:
		if not p.slot:
			no_slots.append(p)
	return no_slots


'''

def check_empty(problem):
	empty_domain = []
	for p in problem.pieces:
		if not p.times:
			empty_domain.append(p)
	return empty_domain


def relax_constraints_before(problem, invalid_pieces):

#remove dancers with very few time slots (indication that they are busy)
	#print ('invalid_pieces', [p.choreographer.name for p in invalid_pieces])
	for p in invalid_pieces: 
		#print ('invalid p', p.choreographer.name)
		if p.performers:
			dancer_counts = []
			for dancer in p.performers:
				dancer_counts.append((dancer, len(dancer.availability)))
			#is_empty = check_empty(problem)
			#print ('dancer_counts', [x[1] for x in])
			while not p.times:
				busiest_dancer = (min(dancer_counts, key = lambda x: x[1]))
				p.remove_dancer(busiest_dancer[0])
				dancer_counts.remove(busiest_dancer)
				problem.violations.append((busiest_dancer[0].name, p.choreographer.name))
				p.times = [x for x in p.choreographer.availability if x in problem.domain]
				#problem = Scheduler(problem.dancers, problem.pieces, problem.violations)
				#print ('len dancers',len(problem.dancers))
				problem.set_initial(problem.pieces, problem.dancers)
		else:
			p.choreographer.availability = problem.domain
			p.times = p.choreographer.availability
			problem.set_initial(problem.pieces, problem.dancers)
		


def solve(dancers, pieces, domain, algorithm, randomness = False):
	problem = Scheduler(dancers, pieces, domain)
	problem.set_initial(pieces, dancers)
	invalid_pieces = check_empty(problem)
	if invalid_pieces:
		relax_constraints_before(problem, invalid_pieces)

	if algorithm == 'naive':
		problem.set_times(pieces)

	elif algorithm == 'backtracking':
		output = problem.assign_backtracking(pieces)
		while not output:
			problem.relax_constraints_after(randomness)
			output = problem.assign_backtracking(pieces)



	elif algorithm == 'DFS':
		output = problem.DFS(pieces)
		while not output:
			problem.relax_constraints_after(randomness)
			output = problem.DFS(pieces)

	problem.set_slots()

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
			print ("{} cannot attend {}'s piece".format(v[0], v[1]))
	#return problem


#python scheduler.py simple DFS


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





#evaluate branching factor
#fix pre relaxing
#allo hardcoded rehearsal slots
#get random solution
#define better solution function
#evaluate heuristic
#implement timer
#guest choregrapher
#implement randomness
