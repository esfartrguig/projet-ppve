from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    return render_template('result.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)