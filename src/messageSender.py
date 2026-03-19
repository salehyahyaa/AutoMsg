import subprocess
"""
AppleScript's way of exectuing commands on macOS applications to allow us to send msgs from our software to Imessege's
"""

class MessageSender: 
    def __init__(self): 
        pass 

    def send(self, phoneNumber, message):
        apple_script = f'''
        tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy "{phoneNumber}" of targetService
            send "{message}" to targetBuddy
        end tell
        '''
        subprocess.run(["osascript", "-e", apple_script]) #osascript-> macOS tool, -e -> execute 
        

