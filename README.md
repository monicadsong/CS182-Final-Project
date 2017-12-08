# CS182-Final-Project

## A CSP-Based Rehearsal Scheduler
### Monica Song, monicasong@college.harvard.edu

To run the scheduler, type: 
`python solver.py <show> <algorithm>`
where `<show>` can be `InPassage`, `Oz`, or `CityScapes` and `<algorithm>` can be `DFS`, `heuristic`, or `random`.

To evaluate an existing tech week, type:
`python eval_solution.py <show>`

#### Description of the files:
* *solver.py*: runs the scheduler
* *scheduler.py*: contains the code for the scheduler class and the three algorithms
* *eval_solution.py*: evaluates a pre-existing actual tech week
* *classes.py*: contains the Dancer and Rehearsal classes
* *helper.py*: contains helper functions referenced by the Scheduler class
* *timeslot_vars.py*: contains the variable values for the time slots
* *Tree.py*: contains helper code for building the search tree
* *InPassage.py, CityScapes.py, Oz.py*: contain the dancer and piece objects for each performance
