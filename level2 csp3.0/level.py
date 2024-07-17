from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')
@app.route('/x')
def x_route():
    return "This is the /x route!"
if __name__ == '__main__':
    app.run(debug=False)
