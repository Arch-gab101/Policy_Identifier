# replicate current inbound flow policy application
# As a start we will focus on CEX and Blocked Senders Policy to test detection and reporting.
# develop a flow from terminal and later advance to GUI

import datetime, time, string

mail_from = input("Enter Your Email")


#Block Sender Policy
block_sender = ['gmail.com'] #block everything coming inbound from gmail.com
array = []

for mail in mail_from.split("@"):
    array.append(mail)
    
if array[1] in block_sender:
    print('mail blocked')
else:
    print('Allowed through')