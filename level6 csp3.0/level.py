from flask import Flask, render_template, redirect, make_response
import base64
import os

app = Flask(__name__)

@app.route('/')
def main_page():
    return redirect("/frame#/static/gadget.js")

@app.route('/frame')
def frame_page():
    nonce = base64.b64encode(os.urandom(16)).decode('utf-8')
    response = make_response(render_template('index.html', nonce=nonce))
    csp_policy = f"default-src 'self'; script-src 'self' 'nonce-{nonce}'; img-src 'self' data:; style-src 'self';"
    response.headers["Content-Security-Policy"] = csp_policy
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
