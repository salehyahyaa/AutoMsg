from messageSender import *
from contacts import *                        #never import * in a real world scnerino, here its ok
from messages import * 

iMsgSender = MessageSender()                            #we instaintate a class as setup when we want to start instainizating objects from it


def send_messege(holiday, group): 
    message = msgs[holiday][group]                      #must be this way since our data is nested within dict

    for name, phoneNumber in contacts[group].items(): #the standard/defualt is when you loop through a dict it only returns the keys, so we call items() to return the key value pairs #phoneN
        if phoneNumber:                               #if the value isnt empty || none
            print(f"Sending msg to {name}")
            iMsgSender.send(phoneNumber, message)
    


send_messege("eid", TESTING)




