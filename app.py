import eventlet
eventlet.monkey_patch()from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacker_secret_123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Mesaj Alındı: ' + msg)
    # Mesajı herkese gönder
    emit('message', msg, broadcast=True)

@socketio.on('image')
def handle_image(data):
    # Görsel verisini herkese yayar
    emit('image', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
