To setup and run Flask server locally through CLI, follow these steps:

# Setup

- make sure FLAC converson utility is installed on your system: 
  - Windows command: PS> flac --version
  - Mac/Linux command: $ flac --version
- if FLAC is not installed on system:
  - Windows: go to [FLAC official system ](https://xiph.org/flac/download.html) and follow official installation instructions
    - Make sure to add the directory containing flac.exe to your PATH environment variable so that you can run the flac command from any command prompt
  - Linux (Ubuntu/Debian) command: sudo apt-get install flac
  - Mac command: brew install flac
    - if you dont' have Homebrew installed, run: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- create Python virtual environment (note: you don't actually have to create the virtual environment if cloning this repo since it's included in the directory - do make sure to go through the following steps however to install the packages into the environment ACTUALLY WILL HAVE TO UPDATE THIS TO REMOVE VENV FROM GIT)
  - Windows command: PS> python -m venv speech-recognition-env
  - Mac/Linux command: $ python3 -m venv speech-recognition-env
- activate Python virtual environment
  - Windows command: PS> \Scripts\activate
  - Mac/Linux command: $ source speech-recognition-env/bin/activate
- install packages into virtual environment
  - python3 -m pip install flask
  - python3 -m pip install SpeechRecognition
  - python3 -m pip install nltk
    - open Python console with command "python3" in terminal
    - in Python console, run the following commands
      - import nltk
      - nltk.download('vader_lexicon')

# Run application in dev server

- activate Python virtual environment if not already activated
  - Windows command: PS> \Scripts\activate
  - Mac/Linux command: $ source speech-recognition-env/bin/activate
- run application
  - $ python3 app.py


(there are some included audio files in the static directory in the repo that can be used for testing)

# Stop running application

- Press CTRL+C in CLI to close dev server
- Deactivate Python virtual environment
  - Windows command: (speech-recognition-env) PS> deactivate
  - Mac/Linux command: (speech-recognition-env) $ deactivate
