import inPassage
import simple_example
import CityScapes
import Oz

import random

def crossOff(rehearsal_times, dancer_times):
	"""
	Removes unavailable dancer times from rehearsal times
	"""
	#dancer times is a list of dancer's available times
	#rehearsa times is the list of the choreographer's available times
	new_rehearsal_times = rehearsal_times[:]
	for r in rehearsal_times:
		if r not in dancer_times:
			new_rehearsal_times.remove(r)
	return new_rehearsal_times
   

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
				p.times = crossOff(p.times, d.availability)
			print ('the times avail for {} piece are'.format(p.choreographer.name), p.times)

	#set_initial(self.pieces, self.dancers)

	def set_times(self, pieces):
		#iterate through the remaining times in each rehearsal
		#naively assign the first times
		for p in pieces:
			print ("the times available for {} piece are {}".format(p.choreographer, p.times))
			if p.times:
			#set rehearsal time to the first time
				p.slot = p.times[0]
			for x in pieces:
				if p.slot in x.times:
					x.times.remove(p.slot)

	# USING HEURISTIC
	def assign_backtracking(self, pieces):
		#helper function to check if no legal values remain
		def check(pieces, slot):
			for p in pieces:
				if slot in p.times:
					if len(p.times) == 1:
						return False
			return True

		#def remove(pieces, slot):


		#order the pieces by number of slots remaining, least first
		order = sorted(pieces, key=lambda x: len(x.times))
		names = [x.choreographer.name for x in order]
		print ("the order of assignments is {}".format(names))

		time_counts = {}
 
		#find the least constraining value
		for p in pieces:
			for t in p.times:
				if t in time_counts:
					time_counts[t] += 1
				else:
					time_counts[t] = 1
		print ("time_counts_dict {}".format(time_counts))

		for i,p in enumerate(order):
			values = [(x, time_counts[x]) for x in p.times]
			print ("values", values)
			while values:
				#get the least constraining value
				lcv = min(values, key=lambda x: x[1])
				p.slot = lcv[0]
				print ("the least constraining value is {}".format(p.slot))
				#remove the valuses frmo 
				values.remove(lcv)
				#remove the value from all other variables
				if check(pieces[i:], p.slot):
					#print ("The assigned time for {} piece is {}".format(p.choreographer, p.slot))
					for x in pieces[i:]:
						if p.slot in x.times:
							x.times.remove(p.slot)
					break
			#print ("Unable to assign time slot to {} rehearsal".format(p.choreographer))
			#else:
				#assign the next least constraining value
		#return False
	#def arc_consistency:
			 #go through all permutations of variable ordering
			 #if any permuation results in an empty domain, skip
			 #unnecessary because of the tree like structure


	def DFS(self, pieces):
		

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
		#create search tree
		for p in pieces:
			#print ("p.choreographer.name", p.choreographer.name)
			#print ("p.times", p.times)
			successors = []
			for t in p.times:
				new_node = Node(p.choreographer, t)
				successors.append(new_node)
			for c in current:
				c.add_successors(successors)
			current = successors

		solutions = []
		sol_scores = []
		#traverse tree
		stack = [start]
		while stack:
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
		best = min(sol_scores, key=lambda x: x[0])[0]
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
			if random.random() > 0.4:
				biggest_piece = random.choice(self.pieces)

		print ('biggest_piece', biggest_piece.choreographer.name)
		overlap = find_most_constraining(biggest_piece)
		most_constraining_dancer = (min(overlap, key = lambda x: x[1]))[0]
		
		print ('most contraining dancer', most_constraining_dancer.name, most_constraining_dancer.availability)
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

		return nonharvard_score + dinner_score + late_score




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
	print ('invalid_pieces', [p.choreographer.name for p in invalid_pieces])
	for p in invalid_pieces: 
		print ('invalid p', p.choreographer.name)
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
				p.times = p.choreographer.availability
				#problem = Scheduler(problem.dancers, problem.pieces, problem.violations)
				print ('len dancers',len(problem.dancers))
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
		problem.assign_backtracking(pieces)


	elif algorithm == 'DFS':
		output = problem.DFS(pieces)
		while not output:
			problem.relax_constraints_after(randomness)
			for p in pieces:
				print ('dancers in {}'.format(p.choreographer.name), [x.name for x in p.performers])
			output = problem.DFS(pieces)

	problem.set_slots()

	for p in pieces:
		if p.slot:
			print ("the assigned time for {} piece is {}".format(p.choreographer.name, p.slot))
		else:
			print ("Unable to assign time slot to {} rehearsal".format(p.choreographer.name))
	#get each dancer's schedule
	#print ('hello')
	for d in dancers:
		print ("{} has these times scheduled: {}".format(d.name, d.times))
	print ('violations', problem.violations)
	return problem

#solve(inPassage.dancers2, inPassage.pieces2, inPassage.domain, 'DFS')
#solve(simple_example.dancers, simple_example.pieces,simple_example.domain,'DFS')
#solve(CityScapes.dancers, CityScapes.pieces, CityScapes.domain, 'DFS')
def evaluate(problem):
	num_violation = len(problem.violations)
	score = problem.evaluate()
	print ('violations', num_violation)
	print ('score', score)

problem = solve(inPassage.dancers2, inPassage.pieces2, inPassage.domain, 'backtracking')
evaluate(problem)




#to do: make examples
#allo hardcoded rehearsal slots
#get each dancers schedule
#get random solution
#implement timer
#guest choregrapher
