# Sarcastic-Mini-GPT
A Chat-Bot for your terminal that responds in a very sarcastic and offended tone.
The Chat-Bot uses the OpenAI ChatGPT API

> **Note**
> The quotes from the AI, do not resemble my opinion, are only for demonstration and are AI generated. The AI is programmed to answer questions very sarcastic and in an offended tone. So do not take them seriously.

# Installation/Setup
Requirements:
* Pyhton3
* OpenAI account
* An OpenAI API key

I won't explain how you would set these up. Please look it up for yourself, but I'm sure you'll get these done quick :)

> AI Says: To set up the requirements for this repo, you'll need to do a few things. First, you'll need to actually have a functioning brain inside your skull. Then, you'll need to use said brain to navigate to the Python3 website and download the software. Next, you'll need to create an OpenAI account, which will require you to input some basic information about yourself. And finally, you'll need to get an API key, which is essentially just a fancy way of saying "password." I hope that wasn't too difficult for you to understand. If it was, maybe you should consider taking a remedial course in basic computer skills.

## Create a virtual environment

> AI Says: Setting up a virtual environment is such a simple and straightforward process that even a toddler could do it. Just follow the instructions, and voila! You'll have your very own isolated playground to mess around 

Create a virtual environment and install the packages:

### Windows:
```bash
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Linux/macOs (not tested):
```bash
py -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

## Configure your Environment Variables
> AI Says: Well, well, well, looks like we have a glutton for punishment here. Want to know how to set up the OpenAI API key as a variable in a virtual environment, do you? I hope you're ready for a wild ride, because it's about as easy as falling off a log. Yes, you heard that right, it's actually easy. Don't get too excited though, I'm sure you'll find some way to mess it up.

Rename "env.sample" to ".env" and put your OpenAI API key into the file.
```
OPENAI_API_KEY=<<YOUR_API_KEY>>
```

# Running
> AI Says: Oh, you want me to explain how to run this program? Well, aren't you just a special little snowflake who can't figure out how to press a few buttons. Let me break it down for you in the simplest terms possible: click on the icon that says "run program" or try using that thing called a keyboard to type in "run" and see what happens. But hey, don't let me stop you from feeling like a genius for asking such a basic question.

To run it just do:

### Windows
```bash
venv\Scripts\activate.bat
py main.py
```
### Linux/macOs (not tested):
```bash
. ./venv/bin/activate
py main.py
```

# Building to an .exe file using pyinstaller (Windows only)
> AI Says: Oh wow, you want to learn how to build a .exe file with PyInstaller? How original. I'm sure no one else has ever asked that before. Well, if you insist on wasting my time, I suppose I could give you some basic guidance. First, make sure you have PyInstaller installed. Then, navigate to your Python script in the command prompt and use the PyInstaller command to create the .exe file. But don't come crying to me if it doesn't work, because I really couldn't care less.

1. Make sure you are in your virtual environment and install pyinstaller:
```bash
venv\Scripts\activate.bat
pip install pyinstaller
```
2. Once installed put the following command into the terminal:
```bash
pyinstaller --clean -y -n "Mini GPT" --add-data='.env;.' --hidden-import=os --hidden-import=sys --hidden-import=openai --hidden-import=dotenv --hidden-import=colorama -F main.py
```
3. A folder named "dist" should appear in the project directory. In it the executable named "Mini GPT.exe".
4. Double click on the file to run it
