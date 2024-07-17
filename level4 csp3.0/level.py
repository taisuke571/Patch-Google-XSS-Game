from flask import Flask, render_template, request, g
import secrets

app = Flask(__name__)

@app.before_request
def generate_nonce():
    g.nonce = secrets.token_urlsafe(16)


@app.route('/', methods=['GET'])
def main_page():
    timer = request.args.get('timer')
    if not timer:
        return render_template('index.html', nonce=g.nonce)
    else:
        return render_template('timer.html', timer=timer, nonce=g.nonce)

@app.after_request
def apply_csp(response):
    csp_policy = f"default-src 'self'; script-src 'self' 'nonce-{g.nonce}'; worker-src 'self'; manifest-src 'self'; report-to 'default';"
    response.headers["Content-Security-Policy"] = csp_policy
    return response

if __name__ == "__main__":
    app.run(debug=True)
