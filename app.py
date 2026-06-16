from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return jsonify({
        "mensaje": "El servidor sirve profesor",
        "host": hostname,
        "status": "online"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
