from flask import Flask, render_template, request, url_for

app = Flask(__name__)

from urllib.parse import urlparse

def sanitize_next_url(next_url):
    # Parse the URL to extract the scheme
    parsed_url = urlparse(next_url)

    # Disallow certain schemes known for XSS attacks
    disallowed_schemes = ['javascript', 'data', 'vbscript']
    if parsed_url.scheme in disallowed_schemes:
        return url_for('main_page', path='welcome')

    # Additional checks can be added here as needed

    return next_url


@app.route('/<path:path>', methods=['GET'])
def main_page(path):
    next_url = request.args.get('next')
    sanitized_next_url = sanitize_next_url(next_url)

    if "signup" in path:
        return render_template('signup.html', next=sanitized_next_url)
    elif "confirm" in path:
        return render_template('index.html', next=sanitized_next_url or 'welcome')
    else:
        return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
