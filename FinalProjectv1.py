import inPassage
import simple_example

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
	def __init__(self, dancers, pieces, violations = []):
		#all dancers
		self.dancers = dancers
		self.pieces = pieces
		self.violations = violations


		for p in pieces:
			for d in p.performers:
				#wow big mistake
				p.times = crossOff(p.times, d.availability)

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

	def remove(self, choreographer, dancer):
		for p in self.pieces:
			if p.choreographer.name == choreographer:
				print ('FOUND')
				p.performers.remove(dancer)
				break
		self.set_initial(self.pieces, self.dancers)
		print ('p.name', p.choreographer.name)
		print ('p.times', p.times)
		return p.times
	

	

	def relax_constraints_before(self, invalid_pieces):

	#remove dancers with very few time slots (indication that they are busy)
		print ('invalid_pieces', [p.choreographer.name for p in invalid_pieces])
		for p in invalid_pieces: 
			dancer_counts = []
			for dancer in p.performers:
				dancer_counts.append((dancer, len(dancer.availability)))
			print ('dancer_counts', [x[1] for x in dancer_counts])
			while not p.times: 
				print ('iteration')
				busiest_dancer = (min(dancer_counts, key = lambda x: x[1]))
				self.remove(p.choreographer.name, busiest_dancer[0])
				dancer_counts.remove(busiest_dancer)
				self.violations.append((dancer.name, p.choreographer.name))
				
				print ('p.perfomers', [x.name for x in p.performers])

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
			print ("p.choreographer.name", p.choreographer.name)
			print ("p.times", p.times)
			successors = []
			for t in p.times:
				new_node = Node(p.choreographer, t)
				successors.append(new_node)
			for c in current:
				c.add_successors(successors)
			current = successors

		solutions = []

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

		if solutions:
			for i,s in enumerate(solutions):
				print ("Solution {}: {}".format(i, s))
		else:
			print ('no valid assignment found')

		#return solutions


		#rate solutions
		sol_scores = []
		for s in solutions:
			self.assign_solution(s)
			sol_scores.append((s, self.evaluate()))
		#get minimum score solution
		best = min(sol_scores, key=lambda x: x[0])[0]
		print ('best',best)
		self.assign_solution(best)


	
	def relax_constraints():
		pass
			#remove a dancer's availability frm 





	def assign_solution(self, solution):
		for p, time in zip(self.pieces, solution):
			p.slot = time
		for d in self.dancers:
			d.times = []
			for p in self.pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)
		

	def set_slots(self):
		for d in self.dancers:
			d.times = []
			d.pieces = []
			for p in self.pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)
					d.pieces.append(p.choreographer.name)
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
				for i,t in enumerate(d.times[:1]):
					if t.split('.')[0] == d.times[i+1].split('.')[0]:
						if abs(int(t.split('.')[1]) - int(d.times[i+1].split('.')[1])) > 2:
							nonharvard_score += 1
			hours = [int(x.split('.')[1]) for x in d.times]
			#print (hours)
			if 5 in hours and 6 in hours:
				print ('dancer dinner', d.name)
				dinner_score += 2

		times = [int(p.slot.split('.')[1]) for p in self.pieces]
		for t in times:
			if t > 10:
				late_score += 1

		return nonharvard_score + dinner_score + late_score





def has_slot(problem):
	no_slots = []
	for p in problem.pieces:
		if not p.slot:
			no_slots.append(p)
	return no_slots

def get_dancer_count(pieces):
	counts = []
	for p in pieces:
		len(p.performers)

def check_empty(problem):
	empty_domain = []
	for p in problem.pieces:
		if not p.times:
			empty_domain.append(p)
	return empty_domain




	#return violations




def relax_constraints_after(problem):
	#remove the dancer from the piece with the most dancers
	#remove dancers who are in a lot of pieces
	pass

def solve(dancers, pieces, algorithm):
	problem = Scheduler(dancers, pieces)
	problem.set_initial(pieces, dancers)
	invalid_pieces = check_empty(problem)
	if invalid_pieces:
		problem.relax_constraints_before(invalid_pieces)

	if algorithm == 'naive':
		problem.set_times(pieces)

	elif algorithm == 'backtracking':
		problem.assign_backtracking(pieces)

	elif algorithm == 'DFS':
		problem.DFS(pieces)

	problem.set_slots()

	for p in pieces:
		if p.slot:
			print ("the assigned time for {} piece is {}".format(p.choreographer.name, p.slot))
		else:
			print ("Unable to assign time slot to {} rehearsal".format(p.choreographer.name))
	#get each dancer's schedule

	for d in dancers:
		print ("{} has these times scheduled: {}".format(d.name, d.times))


#print (inPassage.Sat1)
solve(inPassage.dancers2, inPassage.pieces2, 'DFS')
#solve(simple_example.dancers, simple_example.pieces,'DFS')




#to do: make examples
#allo hardcoded rehearsal slots
#get each dancers schedule
# allow no's and maybes

#add domain
#what if neither the dancers or choreographers have overlapping times-- choose the dancer with 
	 