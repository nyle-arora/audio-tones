from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# creates route to home page
@app.route("/", methods=['GET', 'POST'])
# defines what is returned on home page
def index():
    # if post request is created through index.html page, be able to act on form data
    if request.method == "POST":
        print("form data received")

    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    # debug = true allows flask instance to refresh with the latest updates
    # threaded = true allows app to process multiple requests at same time
    app.run(debug=True, threaded=True)