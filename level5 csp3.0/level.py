from flask import Flask, render_template, request

app = Flask(__name__)
CSP_POLICY = " default-src 'self'; script-src 'self' 'nonce-random-value-here';img-src 'self' data:; object-src 'none'; form-action 'self';"

@app.after_request
def apply_csp(response):
    response.headers["Content-Security-Policy"] = CSP_POLICY
    return response
@app.route('/<path:path>', methods=['GET'])
def main_page(path):
    if "signup" in path:
        return render_template('signup.html', next=request.args.get('next'))
    elif "confirm" in path:
        return render_template('index.html', next=request.args.get('next', 'welcome'))
    else:
        return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
