def calculateEV(prob1, prob2, odds1, odds2, prob3=0, odds3=0, prob4=0, odds4=0):
	return prob1*odds1 + prob2*odds2 + prob3*odds3 + prob4*odds4

def arb(prob1, prob2, odds1, odds2):
	arb = 1/odds1*100 + 1/odds2*100
	if( arb < 1):
		return True
	return False
	