from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'funcionando'

app.run(debug=True)