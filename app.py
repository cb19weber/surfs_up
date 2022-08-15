# Import Flask
from flask import Flask

# Create an application instance
app = Flask(__name__)

# Establish Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

