from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main_page():
    return redirect("/frame#/static/gadget.js")

@app.route('/frame')
def frame_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
