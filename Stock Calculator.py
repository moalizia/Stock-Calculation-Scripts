print("This program displays the profit/loss of owned and sold stocks")
print("Made by Mohammed Ali Zia")

print("............................................................")

print("For maximum ease, list all the names of your stocks in a spreadsheet program and below it, type in the buying price, selling price and the amount of stocks")
print("Thus when asked in this program about stocks, there will be a less chance of misinformation typed in.")

print("............................................................")

# Improvements to add:-
# ->Clean up the display
# ->Make less wordy
# ->Make continuous program (No need to exit and restart to use again)
# ->Possible GUI display?


#-----------------------------------------------------------------------------------------------------------------------
questname_done = 0
stockname_list = []
while questname_done == 0:
    stock_name = input("What is the name/code of your Stock?") # Stock question
    stockname_list.append(stock_name) # Stock addition

    question_correctinput = 0
    while question_correctinput == 0:
        question_continue = input("Do you want to add more stocks? Enter 'Yes' or 'No'.") # Stock add continue question
        if question_continue == "Yes" or question_continue == "yes" or question_continue == "Y" or question_continue == "y" or question_continue == "YES": # Positive reply
            question_correctinput = 1
            questname_done = 0
        elif question_continue == "No" or question_continue == "no" or question_continue == "N" or question_continue == "n" or question_continue == "NO": # Negative reply
            question_correctinput = 1
            questname_done = 1
        else: # Redundant reply
            print("Please give a valid input!")
            question_correctinput = 0
            questname_done = 0

# Stock Names are now placed into a list

#-----------------------------------------------------------------------------------------------------------------------
stockIP_list = []
stockFP_list = []
stockNum_list = []
for index in range(len(stockname_list)):
    stockIPGO = 0
    while stockIPGO == 0:
        try:
            stockIPadd = float(input("Enter " + stockname_list[index] + "'s buying price. Please enter a number!"))
        except ValueError:
            print("Invalid Data Type entered!")
            stockIPGO = 0
        except:
            print("Something went wrong!")
            stockIPGO = 0
        else:
            stockIPGO = 1
    stockIP_list.append(stockIPadd) # Stock addition
    stockFPGO = 0
    while stockFPGO == 0:
        try:
            stockFPadd = float(input("Enter " + stockname_list[index] + "'s selling price. Please enter a number!"))
        except ValueError:
            print("Invalid Data Type entered!")
            stockFPGO = 0
        except:
            print("Something went wrong!")
            stockFPGO = 0
        else:
            stockFPGO = 1
    stockFP_list.append(stockFPadd) # Stock addition
    stockNumGO = 0
    while stockNumGO == 0:
        try:
            stockNumadd = int(input("Enter " + stockname_list[index] + "'s amount number. Please enter an integer!"))
        except ValueError:
            print("Invalid Data Type entered!")
            stockNumGO = 0
        except:
            print("Something went wrong!")
            stockNumGO = 0
        else:
            stockNumGO = 1
    stockNum_list.append(stockNumadd) # Stock addition

# Stock Initial Prices are now put in a list
# Stock Final Prices are now put in a list
# Stock Amounts are now put in a list

print("-----------------------------------------------------------------------------------------------------------------")

print("Your stock names respectively are ", stockname_list)
print("Your stock buying prices respectively are ", stockIP_list)
print("Your stock selling prices respectively are ", stockFP_list)
print("Your stock amounts respectively are ", stockNum_list)

print("-----------------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------
# First the loop to calculate the net gains
stockGain_list = []
for index1 in range(len(stockname_list)):
    Amount = stockNum_list[index1]
    SellingPrice = stockFP_list[index1]
    BuyingPrice = stockIP_list[index1]
    stockGain_value = (Amount)*(SellingPrice-BuyingPrice)
    stockGain_list.append(stockGain_value)

# Second the display for Name, Initial Price, Final Price, Amount & Gain for each stock value
for index2 in range(len(stockname_list)):
    print(str(stockname_list[index2]) + " gives a net gain of " + str(stockGain_list[index2]) + " for " + str(stockNum_list[index2]) + " stocks.")
    print("-----------------------------------------------------------------------------------------------------------------")

# Third the total gain(positive)/loss(negative)
stock_netgain = 0
for index3 in range(len(stockname_list)):
    stock_netgain = stock_netgain + stockGain_list[index3]

print("Your total net gain is ", stock_netgain)
# End of program

Program_Exit = input("Press ENTER to exit the program.")

#-----------------------------------------------------------------------------------------------------------------------


