import os
from flask import Flask

# initialization
app = Flask(__name__)

# controllers
@app.route("/")
def hello():
	return "Hello from Python!"

'''
# launch
if __name == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

'''