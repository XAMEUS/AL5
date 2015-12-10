def predToAdj(l):
	adj = []
	for n in l:
		adj[n[1]].append(n[0])

def adjToPred(l):
	for e in l:
		for 