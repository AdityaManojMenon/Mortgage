#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:42:58 2023

@author: adi
"""
###########################################################
    #  Computer Project #3
    #The program asks the user to input some answers to a series of inputs which is used to calculate the mortgage. 
    #Then the program suggests whether the user can offered the mortgage. 
    #Then the program asks the user if they want to print out a table that displays several important values for monthly payment. 
    #Then the program asks the user if they wanr to repeat the progam.

    ###########################################################
NUMBER_OF_PAYMENTS = 360
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

''' WRITE YOUR CODE USING THE CONSTANT VALUES ABOVE '''
attempt = "Y" or "y"
locations=("Seattle", "San Francisco", "Austin", "East Lansing")
# The loop only runs when attempt is "Y" OR "y"
while attempt == "Y" or attempt == "y":
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
    print("\nEnter a value for each of the following items or type 'NA' if \
unknown ")
#Asks the user to input important values for calculations
    location = input("\nWhere is the house you are considering (Seattle, \
San Francisco, Austin, East Lansing)? ")
    area = input("\nWhat is the maximum square footage you are considering? ")
    monthly_payment = input("\nWhat is the maximum monthly payment you can \
afford? ")
    down_payment=input("\nHow much money can you put down as a down payment? ")
    apr = input("\nWhat is the current annual percentage rate? ")
#The code checks determines what tax rate to use and price per square feet based on location.   
    if location == "East Lansing":
        tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
        price_per_sqft = EAST_LANSING_PRICE_PER_SQ_FOOT
        print("\n")
    elif location == "Seattle":
        tax_rate = SEATTLE_PROPERTY_TAX_RATE
        price_per_sqft = SEATTLE_PRICE_PER_SQ_FOOT
        print("\n")
    elif location == "San Francisco":
        tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
        price_per_sqft = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        print("\n")
    elif location == "Austin":
        tax_rate = AUSTIN_PROPERTY_TAX_RATE
        price_per_sqft = AUSTIN_PRICE_PER_SQ_FOOT
        print("\n")
    else:
        tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        price_per_sqft = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        print("\nUnknown location. Using national averages for price per \
square foot and tax rate.\n\n")
#Runs calculation if the user knows the area and inputs it.
    if area!="NA":
        area=float(area)
        price_per_sqft=float(price_per_sqft)
        cost = (area * price_per_sqft)
        loan_amount= cost-float(down_payment)
        monthly_tax= (cost*tax_rate)/12
        if apr=="NA":
            apr=APR_2023
        else: 
            apr=float(apr)/100

        if down_payment=="NA":
            down_payment=0
        else:
            down_payment=float(down_payment)
        mpr=apr/12
        monthly_tax= (cost*tax_rate)/12
        mortgage_payment=loan_amount*(mpr*(1+mpr)**360)/(((1+mpr)**(360)-1))  

        
#Runs the calculation if the user knows their max monthly payment
        if monthly_payment!= "NA":
            if location in locations:
                monthly_payment=float(monthly_payment)
                total= mortgage_payment+monthly_tax
                apr=apr*100
                print("In {}, an average {} sq. foot house would \
cost ${}.".format((location),int(area),int(cost)))
                print('''A 30-year fixed rate mortgage with a down payment of\
 ${} at {}% APR results\n\tin an expected monthly payment of ${:.2f} (taxes)\
 + ${} (mortgage payment) = ${:.2f}'''.format(int(down_payment),\
round(apr,1),monthly_tax,(round(mortgage_payment,2)),round(total,2)))
            else:
                monthly_payment=float(monthly_payment)
                total= mortgage_payment+monthly_tax
                apr=apr*100              
                print("In the average U.S. housing market, an average {} sq. \
foot house would cost ${}.".format(int(area),int(cost)))
                print('''A 30-year fixed rate mortgage with a down payment \
of ${} at {}% APR results\n\tin an expected monthly payment of ${:.2f} \
(taxes) + ${} (mortgage payment) = ${:.2f}'''.format(int(down_payment),\
round(apr,1),monthly_tax,(round(mortgage_payment,2)),round(total,2)))
#Outputs the result based on imputs and compares with monthly payment in order to determine if the user can offord the mortgage  
            if total>monthly_payment:
                print("Based on your maximum monthly payment of ${:.2f} you \
cannot afford this house.".format(round(monthly_payment)))
            else:
                print("Based on your maximum monthly payment of ${:.2f} you \
can afford this house.".format(round(monthly_payment)))

            balance= cost-down_payment
            interest=loan_amount*mpr
            principal=mortgage_payment-interest
            schedule = input("\nWould you like to print the monthly payment \
schedule (Y or N)? ")  
            if schedule== "Y" or schedule== "y":
                print("\n Month |  Interest  |  Principal  |   Balance    \
\n================================================")

                for i in range(360):
                    print("{:^7}| ${:>9.2f} | ${:>10.2f} | \
${:>11.2f}".format(i+1,interest,principal,balance))
                    balance-=principal
                    interest=balance*mpr
                    principal=mortgage_payment-interest
                
        
        else:   
            monthly_tax= (cost*tax_rate)/12
            mortgage_payment=loan_amount*(mpr*(1+mpr)**360)/((1+mpr)**(360)-1)
            total= mortgage_payment+monthly_tax
            apr=apr*100    
            print("In {}, an average {} sq. foot house \
would cost ${}.".format((location),int(area),int(cost)))
            print('''A 30-year fixed rate mortgage with a down payment of ${}\
 at {}% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) + ${} \
(mortgage payment) = ${:.2f}'''.format(int(down_payment),round(apr,1),\
 round(monthly_tax,2),(round(mortgage_payment,2)),round(total,2)))  
            balance= cost-down_payment
            interest=loan_amount*mpr
            principal=mortgage_payment-interest
            schedule = input("\nWould you like to print the monthly payment\
 schedule (Y or N)? ")  # if the user inputs y the program will print the table that displays important information about the mortgage.
            if schedule== "Y" or schedule== "y":
                print("\n Month |  Interest  |  Principal  |   Balance    \
\n================================================")

                for i in range(360):
                    print("{:^7}| ${:>9.2f} | ${:>10.2f} | \
${:>11.2f}".format(i+1,interest,principal,balance))
                    balance-=principal
                    interest=balance*mpr
                    principal=mortgage_payment-interest

    else:

        price_per_sqft=float(price_per_sqft)



        if apr=="NA":
            apr=APR_2023
        else: 
            apr=float(apr)/100

        if down_payment=="NA":
            down_payment=0
            
        monthly_payment=float(monthly_payment)
        mpr=float(apr)/12
        down_payment=float(down_payment)
        
        formula=(mpr*(1+mpr)**360)/(((1+mpr)**(360)-1))
        loan=monthly_payment/formula
        cost=int(loan+down_payment)
        mpr=float(apr)/12
        monthly_tax= (cost*tax_rate)/12
        left_area=int(cost/price_per_sqft)
        loan_amount=cost-float(down_payment)
        mortgage_payment=loan_amount*(mpr*(1+mpr)**360)/(((1+mpr)**(360)-1))  
        monthly_payment=round(monthly_payment,2)

        
        print("In {}, a maximum monthly payment of ${} allows\
 the purchase of a house of {} sq. feet for ${}\n\t assuming a 30-year fixed\
 rate mortgage with a ${} \
down payment at {}% APR.".format(location, format(monthly_payment,'.2f'),\
left_area, cost, int(down_payment), format(apr*100,'.1f')))
#Asks the user if he wants to attempt the process again. If they chose 'Y' it does so else it will break and the code will terminate.
    attempt = input("\nWould you like to make another attempt (Y or N)? ")
    if attempt=="N":
        break
    else:
        continue