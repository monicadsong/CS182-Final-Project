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
#arc consistency check if no legal values remain in rest of pieces
def check(pieces, slot):
	for p in pieces:
		if slot in p.times:
			if len(p.times) == 1:
				return False
	return True
#order the pieces by number of slots remaining, least first
#of 

def order(pieces):
	ordered = sorted(pieces, key=lambda x: len(x.times))
	return ordered


def time_counts(pieces):
	counts = {}
	for p in pieces:
		for t in p.times:
			if t in counts:
				counts[t] += 1
			else:
				counts[t] = 1
	#print ("time_counts_dict {}".format(time_counts))
	return counts

def get_dancer_counts(problem):
	dancers = {}
	for p in problem.pieces:
		for d in p.performers:
			if d in dancers:
				dancers[d].append(p)
			else:
				dancers[d] = [p]
