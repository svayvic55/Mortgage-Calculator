# Author: Vichaed Svay
# Date: 1/18/2023
# Description: Mortgage Calculator

# price = float(input("Home Price(P): "))
# downPayment = float(input("Down Payment Amount(D): "))
# loanTerm = float(input("Loan Term In Months(N): "))
# annualInterestRate = float(input("Yearly Interest Rate: "))
# monthlyInterestRate = (annualInterestRate * .01)/12
# 
# priceMinusDown = price - downPayment
# numerator = monthlyInterestRate*((1 + monthlyInterestRate) ** loanTerm)
# denominator = ((1 + monthlyInterestRate) ** loanTerm) - 1
# 
# monthlyPayment = (priceMinusDown)*(numerator/denominator)
# 
# print(monthlyPayment)
import sys
price = float(sys.argv[1])
downPayment = float(sys.argv[2])
loanTerm = float(sys.argv[3])
annualInterestRate = float(sys.argv[4])
monthlyInterestRate = float((annualInterestRate * .01)/12)

priceMinusDown = price - downPayment
numerator = monthlyInterestRate*((1 + monthlyInterestRate) ** loanTerm)
denominator = ((1 + monthlyInterestRate) ** loanTerm) - 1

monthlyPayment = (priceMinusDown)*(numerator/denominator)

print(monthlyPayment)