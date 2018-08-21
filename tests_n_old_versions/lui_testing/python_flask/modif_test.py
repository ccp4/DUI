from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def any_name_works():

    print "txt_2_prn =", txt_2_prn
    str_out = ""
    if request.method == 'POST':
        print request.form

        str_entered = request.form['command']
        str_out = (str_entered + "\n\n") * 5

        print "\n", str_entered, "\n"

    return render_template("index.html", out_put = str_out)

if __name__ == '__main__':
    txt_2_prn = "algun texto"
    app.run(host='0.0.0.0', port=5000)
