To setup and run Flask server locally through CLI, follow these steps:

# Setup

- create Python virtual environment
  - Windows command: PS> python -m venv speech-recognition-env
  - Mac/Linux command: $ python3 -m venv speech-recognition-env
- activate Python virtual environment
  - Windows command: PS> \Scripts\activate
  - Mac/Linux command: $ source speech-recognition-env/bin/activate
- install packages into virtual environment
  - python3 -m pip install flask
  - python3 -m pip install SpeechRecognition

# Run application in dev server

- activate Python virtual environment
  - Windows command: PS> \Scripts\activate
  - Mac/Linux command: $ source speech-recognition-env/bin/activate
- run application
  - $ python3 app.py

# Stop running application

- Press CTRL+C in CLI to close dev server
- Deactivate Python virtual environment
  - Windows command: (speech-recognition-env) PS> deactivate
  - Mac/Linux command: (speech-recognition-env) $ deactivate
