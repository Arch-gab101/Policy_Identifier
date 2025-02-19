# replicate current inbound flow policy application
# As a start we will focus on CEX and Blocked Senders Policy to test detection and reporting.
# develop a flow from terminal and later advance to GUI

import datetime, time, string

mail_from = input("Enter Your Email\n")


#Block Sender Policy
#Can intro a function but for now control flow works
block_sender = {'gmail.com': 'Un_Pol_#01','hotmail.com': 'Un_Pol_#02'} #block everything coming inbound from gmail.com
array = []

for mail in mail_from.split("@"):
    array.append(mail)
    
if array[1] in block_sender.keys():
    print(f'# Mail Rejected due to a Block Sender Policy\n# Policy_ID {block_sender["{}"]}') #fstring to allow for change domains and return correct policy ID
else:
    print('Allowed through')
    