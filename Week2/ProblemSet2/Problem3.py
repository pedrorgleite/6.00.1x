"""
Created on Tue Jul  7 16:37:23 2020
@author: pedro

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year using bisection serach
    
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0
"""
"""
Test case
	      Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
      
                
                  
	      Test Case 2:
	      balance = 999999
	      annualInterestRate = 0.18
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 90325.03
	  
"""


def PayoffPayment(balance, annualInterestRate):

    initialBalance = balance #create a temp value
    lower_bond = balance/12
    upper_bond = (balance*((1+(annualInterestRate/12))**12))/12
    monthlyPayment = (lower_bond + upper_bond)/2 # initate the guess
    # iterate and increase Monthly Payment until the balance is payed off
    while True: 
        balance = initialBalance # set to the intial balance every iteration
        for i in range(12):
            balance = balance - (monthlyPayment) + ((balance - (monthlyPayment))*(annualInterestRate/12))
        if balance<=0.01 and balance>=-0.01:
            break        
        elif balance<0 :
            upper_bond = monthlyPayment
        else:
            lower_bond = monthlyPayment
        monthlyPayment = (lower_bond + upper_bond)/2
    
    return monthlyPayment
    
print(round(PayoffPayment(balance,annualInterestRate),2))
