from flask import Flask, render_template

app = Flask(__name__)
CSP_POLICY = "script-src 'self' ajax.googleapis.com; style-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'self';"

@app.after_request
def apply_csp(response):
    response.headers["Content-Security-Policy"] = CSP_POLICY
    return response

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
