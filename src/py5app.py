from flask import Flask, jsonify
import time
import socket


app = Flask(__name__)

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        "status" : "up"
    })

@app.route('/api/v1/info')
def info():
    return jsonify({
        "time" : time.ctime(),
        "hostname" : socket.gethostname(),
        "message" : "You are doing great, man!",
        "env" : "dev"
    })

if __name__ == '__main__':
    app.run("0.0.0.0")