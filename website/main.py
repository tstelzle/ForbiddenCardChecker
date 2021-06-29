from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/forward/", methods=['POST'])
def check_cards():
    cards = request.form['cards'].replace('\r\n', ';')
    if cards == "":
        return redirect(f"/")
    else:
        try:
            request.form['checkBtn']
            url = 'http://forbiddenCardChecker-api/forbiddenCard/' + cards
            output = json.loads(requests.get(url).json())

            return render_template('result_check.html', matching_results=output[0], typo_results=output[1])
        except KeyError:
            url = 'http://forbiddenCardChecker-api/sampleGame/' + cards
            output = json.loads(requests.get(url).json())

            return render_template('result_sample.html', output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
