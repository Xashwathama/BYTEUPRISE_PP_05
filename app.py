from flask import Flask, render_template, request
import random
import string
import webbrowser
import threading

app = Flask(__name__)

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            password = generate_password(length)
        except ValueError:
            password = 'Invalid input.'
    return render_template('index.html', password=password)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)  # <--- Disable auto-reloader here
