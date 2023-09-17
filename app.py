from flask import Flask, render_template, send_from_directory, request, redirect
import os
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST']) # creates route to home page
# defines what is returned on home page
def index():
    transcript=""
    # act on form data received through POST request in HTML page
    if request.method == "POST": 
        print("form data received")

        #ensure that a valid file is being submitted to the app
        if "file" not in request.files or request.files["file"].filename == "":
            return redirect(request.url)

        if request.files["file"]:
            recognizer = sr.Recognizer() # create instance of Recognizer class from speech recognition library
            audioFile = sr.AudioFile(request.files["file"]) # obtain audio file from file input in form
            # open up audio file and read it through recognizer
            with audioFile as source:
                data = recognizer.record(source) # extract audio data from file
            transcript = recognizer.recognize_google(data, key=None) #transcribe audio data to text using Google speech to text API (only works on wav files tho)

    return render_template('index.html', transcript=transcript)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    # debug = true allows flask instance to refresh with the latest updates
    # threaded = true allows app to process multiple requests at same time
    app.run(debug=True, threaded=True)