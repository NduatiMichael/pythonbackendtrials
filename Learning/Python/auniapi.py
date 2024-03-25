
"""
Load  credit:
1 - Validate the amount and phone number
2 - Validate the telco to be used
3 - Trigger Credit loading or return message
"""
Number = "254706443677"
amount = 200
balance = 300
if len(Number) == 12:
    if amount > 0:
            print("Proceed to load credit")
    else:
        print("Enter a valid amount")
else:
    print("Enter a valid number")


"""
Process credit loading
1 - Trigger the relevant mobile money api
2 - listen for the call back response
3 - update the database if successful
4 - Return a message

"""


"""
validate top up:
1 - Validate phone number length
2 - Validate whether Telco is within the accepted list
3 - Check if user's balance is sufficient to process the top up
4 - Trigger credit disbersment or return a Message
"""
Number = "254706443677"
amount = 200
balance = 300
if len(Number) == 12:
    if amount > 0:
        if amount <= balance:
            print("Proceed to disberse")
        else:
            print("You have insufficient funds. Please top up your account.")
    else:
        print("Enter a valid amount")
else:
    print("Enter a valid number")


"""
Process credit disbersment:
1 - Trigger africastalking API
2 - Listen for the call back
3 - Update the database if successful
4 - Return Message
"""


"""
Bulk Disbersment:
1 - find the sum of the credits to be topped up
2 - Validate the account has enough balance to process the selected batch
3 - Trigger the credit disbersment process
4 - Return success or failed
"""

"""
Currency Conversion
1 - Convert the currecies for cross border loading.
"""


#Saraficom Daraja API



#Airtel money API



#Telkom Kenya API



#Momo API



#Vodacom API


