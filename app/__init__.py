from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

from app import routes