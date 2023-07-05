import math
# This is the initial menu with two options notice* the lower() function to program defensively.

print("Welcome here are your options:")
print ("Type 'Investment' - To calculate the amount of interest you'll earn on your deposit")
print("Type 'bond' - To calculate the amount you'll have to pay on a loan")
binary_menu = input("Please enter either 'Investment' or 'Loan':\n").lower()

# Here is where we make sure there isn't some obscure error message.

while True:
    if binary_menu == "investment":
        print("You have chosen the investment tool calculator\n")
        print("Here are your financial options:")
        print ("Simple Interest - Continually added on the initial amount invested per annum.") 
        print ("Compound Interest - Continually added on the amount contained in the account through each cycle per annum.")
        Amount = int(input("How much are you depositing?:\n"))
        Interest = int(input("How much interest?:\n"))
        Years = int(input("How many years?:\n"))
        Type_of_interest = input("Please Choose 'simple' or 'compound' interest:").lower()
        
        
        if Type_of_interest == "simple":
            print("You have chosen simple interest")
            simple1 = float(Amount*(1+Interest/100*Years))
            simple_rounded = round(simple1,2)
            print(simple_rounded)
            break
                        
        elif Type_of_interest == "compound":
            print("You have chosen compound interest")
            compound1 = float(Amount * math.pow((1+Interest/100),Years))
            compound_rounded = round(compound1,2)
            print(compound_rounded)
            break    
        else: Type_of_interest = input("Invalid input. Please only Choose between 'simple' or 'compound' interest:").lower()
                                     
                   
# This is the second option function for the bond
    
        
    elif binary_menu == "loan":
        print("You have chosen the loan tool calculator\n")
        Loan_Amount = float(int(input("What is the value of the property?:\n")))
        Loan_Interest = float(int(input("How much interest as a percentage?:\n")))
        Loan_percent_monthly = (Loan_Interest/100)/12
        Loan_Years = int(input("How many months do you require to payback the loan?:\n"))
        Loan_formula = (Loan_percent_monthly*Loan_Amount)/(1-(1+Loan_percent_monthly)**(-Loan_Years))
        Loan_rounded = round(Loan_formula,2)
        print("This is the amount you will have to reimbourse every month:")
        print(Loan_rounded)
        break

# This else function is to loop back to the initial options should the user have not put a readable choice.
    
    else: 
        
        binary_menu = input("Invalid - Please only select from two options 'Investment' or 'Loan':").lower()

        



        


























