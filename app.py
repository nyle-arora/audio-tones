from flask import Flask, render_template

app = Flask(__name__)

# creates ruote to home page
@app.route("/", methods=['GET', 'POST'])

# defines what is returned on home page
def index():
    return "hello world"

if __name__ == "__main__":
    # debug = true allows flask instance to refresh with the latest updates
    # threaded = true
    app.run(debug=True, threaded=True)