from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    timer = request.args.get('timer')
    if not timer:
        return render_template('index.html')
    else:
        return render_template('timer.html', timer=timer)

if __name__ == "__main__":
    app.run(debug=True)
