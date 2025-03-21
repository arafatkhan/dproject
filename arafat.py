from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/buddha')
def buddha_quote():
    return render_template('buddha.html')

@app.route('/gandhi')
def gandhi_quote():
    return render_template('gandhi.html')

@app.route('/nazrul')
def nazrul_quote():
    return render_template('nazrul.html')


@app.route('/mohammad')
def mohammad_quote():
    return render_template('mohammad.html')

@app.route('/jesus')
def jesus_quote():
    return render_template('jesus.html')

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
