from flask import Flask, render_template, request
app = Flask(__name__)

from time import sleep

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    str_out = ""
    if request.method == 'POST':
        print request.form

        sleep(1)

        str_entered = request.form['command']

        str_out = (str_entered + "\n\n") * 15

        print "\n", str_entered, "\n"

    return render_template("index.html", out_put = str_out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
