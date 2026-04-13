# AutoMsg
Automated iMessage sender for sending personal messages to groups of contacts (family, friends, etc.). Use case for birthdays, holidays, etc.



## Features
- Send messages to multiple contacts automatically  
- Group-based messaging (family, friends, acquaintances)  
- Different message templates per group  
- Runs locally using the macOS Messages app  



## Using Example Files (Important)
`contacts.py` and `messages.py` are not included for privacy reasons.

To use this project:
1. Rename 
- `contacts.example.py` → `contacts.py`
- `messages.example.py` → `messages.py`
2. Add your own 
- names and phone numbers in `contacts.py`
- message templates in `messages.py`



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



## Installation
1. Clone the repository
```bash
git clone https://github.com/salehyahyaa/AutoMsg.git
cd AutoMsg
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
## How to Run
```
cd src
python3 main.py
```



## License
- This project is licensed under the MIT License - see the LICENSE file for details.