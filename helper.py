def ev(prob1, prob2, odds1, odds2):
	return prob1*odds1 - prob2*odds2

def arb(prob1, prob2, odds1, odds2):
	arb = 1/odds1*100 + 1/odds2*100
	if( arb < 1):
		return True
	return False
	