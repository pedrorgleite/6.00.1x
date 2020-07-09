# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:37:23 2020
@author: pedro

The program should print out one line: the lowest monthly payment that 
will pay off all debt in under 1 year, for example:
    
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
"""
Test case
balance = 2000
annualInterestRate = 2 
"""
def PayoffPayment(balance, annualInterestRate):
    monthlyPayment = 0 # initate the guess
    initialBalance = balance #create a temp value
    # iterate and increase Monthly Payment until the balance is payed off
    while balance > 0: 
        balance = initialBalance # set to the intial balance every iteration
        monthlyPayment += 10
        for i in range(12):
            balance = balance - (monthlyPayment) + ((balance - (monthlyPayment)) \
                                                    * (annualInterestRate/12))
    
    return monthlyPayment
print(PayoffPayment(2000,2)
