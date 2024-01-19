from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>Hello from Replit</h1>'


app.run(host='0.0.0.0', port=81)
