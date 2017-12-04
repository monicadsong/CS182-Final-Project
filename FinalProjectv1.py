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
	def __init__(self, dancers, pieces):
		#all dancers
		self.dancers = dancers
		self.pieces = pieces

	def set_initial(self, pieces, dancers):
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
		best = min(sol_scores, key=lambda x: x[0])[1]
		self.assign_solution(best)


	
	def relax_constraints():
		pass
			#remove a dancer's availability frm 





	def assign_solution(self, solution):
		for p, time in zip(pieces, solution):
			p.slot = time
		for d in dancers:
			d.times = []
			for p in pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)

	def set_slots(self):
		for d in dancers:
			d.times = []
			d.pieces = []
			for p in pieces:
			#print ("p", p)
				if d in p.performers:
					d.times.append(p.slot)
					p.pieces.append(p.choreographer.name)

	def evaluate(self):

		#get dancer assignments
		#self.assign_dancer_times(solution)
		#if nonharvard students must travel on two different days
		nonharvard_score = 0
		#check for dinner breaks
		dinner_score = 0
		#check for super late days (11 pm)
		late_score = 0
		for d in dancers:
			if d.role == 'nonharvard':
				days = [x.split('.')[0] for x in d.times]
				if len(set(days)) > 1:
					nonharvard_score += 3
				#minimize the time difference
				for i,t in enumerate(d.times[:1]):
					if t.split('.')[0] == d.times[i+1].split('.')[0]:
						if abs(t.split('.')[1] - d.times[i+1].split('.')[1]) > 2:
							nonharvard_score += 1

			if 5 and 6 in d.times:
				dinner_score += 1
		for s in solution:
			if s > 10:
				late_score += 1

		return nonharvard_score + dinner_score + late_score


def solve(dancers, pieces, algorithm):
	problem = Scheduler(dancers, pieces)
	problem.set_initial(pieces, dancers)
	if algorithm == 'naive':
		problem.set_times(pieces)

	elif algorithm == 'backtracking':
		problem.assign_backtracking(pieces)

	elif algorithm == 'DFS':
		problem.DFS(pieces)


	for p in pieces:
		if p.slot:
			print ("the assigned time for {} piece is {}".format(p.choreographer.name, p.slot))
		else:
			print ("Unable to assign time slot to {} rehearsal".format(p.choreographer.name))
	#get each dancer's schedule
	problem.set_slots()
	for d in dancers:
		d.pieces = problem.get_dancer_times(d, pieces)
		d.times = [x.slot for x in d.pieces]
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
	 