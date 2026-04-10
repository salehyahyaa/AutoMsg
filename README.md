# AutoMsg
Automated iMessage sender for sending personal messages to groups of contacts (family, friends, etc.). Use case for birthdays, holidays, etc.



## Features
- Send messages to multiple contacts automatically  
- Group-based messaging (family, friends, acquaintances)  
- Different message templates per group  
- Runs locally using the macOS Messages app  



## Contacts File (Important)
`contacts.py` file is not included for privacy and security reasons.

To use this project:
1. add `contacts.py`  
2. Add your own names, phone numbers  


## How It Works
This project uses:
- Python  
- AppleScript (to control the Messages app)  
- subprocess (to execute AppleScript from Python)  



## Flow
```
Python → AppleScript → Messages App → Sends iMessage
```



## Project Structure
```
AutoMsg/
│
├── src/
│   ├── main.py
│   ├── messages.py
│   ├── messageSender.py
│   └── contacts.py
│
├── requirements.txt
├── .gitignore
└── README.md
```



## Limitations

- macOS only (relies on AppleScript and the Messages app)
- Requires iMessage to be configured and logged in
- Cannot send messages if the Messages app is closed or restricted
- No built-in scheduling (messages send immediately)
- Limited error handling for failed message delivery
- Not suitable for large-scale or bulk messaging



## How to Run
```
cd src
python3 main.py
```



## License
- This project is licensed under the MIT License - see the LICENSE file for details.