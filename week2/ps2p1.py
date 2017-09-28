def calcEndBalance(startingBalance, annualInterestRate, monthlyPaymentRate,
                   months=12):
    """ Calculates ending balance, given starting balance, end 1 year.

    Args:
        startingBalance (float, 2 decimals): starting balance
        annualInterestRate (float %, 2 decimals)
        monthlyPaymentRate (float %, 2 decimals)
        months (int): number of months to term the debt

    Returns:
        endingBalance (float, 2 decimals): ending balance after 12 months

    """
    monthlyInterestRate = annualInterestRate / 12
    totalBalance = 0
    totalInterest = 0
    totalPayment = 0

    for i in range(months):
        #print('Month ', i, ' : BegBal: ', startingBalance)

        minPayment = startingBalance * monthlyPaymentRate
        totalPayment += minPayment
        #print('minpayment is ', round(minPayment, 2))
        #print('total payments are ', round(totalPayment, 2))
        unPaidBalance = startingBalance - minPayment
        #print('unpaidBalance is ', round(unPaidBalance, 2))
        interest = unPaidBalance * (monthlyInterestRate)
        #print('interest is ', round(interest, 2))
        totalInterest += interest
        #print('total interest is ', round(totalInterest, 2))
        endingBalance  = unPaidBalance + interest
        startingBalance = endingBalance

        print('Month ', i, ' : EndBal: ', round(endingBalance, 2))
        
    print('Remaining balance: ', round(endingBalance, 2))

        
        


calcEndBalance(42, 0.2, 0.04)
