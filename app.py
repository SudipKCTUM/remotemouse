import os
import pyautogui
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Disable PyAutoGUI fail-safe to avoid it stopping on corner move (optional, but better for remote control)
pyautogui.FAILSAFE = False

app = Flask(__name__)
# Change secret_key for production
app.config['SECRET_KEY'] = 'mouse_controller_secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@socketio.on('mouse_move')
def handle_mouse_move(data):
    # data: { dx: float, dy: float }
    dx = data.get('dx', 0)
    dy = data.get('dy', 0)
    pyautogui.moveRel(dx, dy, _pause=False)

@socketio.on('mouse_click')
def handle_mouse_click(data):
    # data: { button: 'left' | 'right' | 'middle' }
    button = data.get('button', 'left')
    pyautogui.click(button=button, _pause=False)

@socketio.on('mouse_scroll')
def handle_mouse_scroll(data):
    # data: { dy: float }
    # PyAutoGUI scroll is platform dependent, scroll(10) is up, scroll(-10) is down
    dy = data.get('dy', 0)
    pyautogui.scroll(int(dy), _pause=False)

@socketio.on('key_press')
def handle_key_press(data):
    # data: { key: string }
    key = data.get('key')
    if key:
        pyautogui.press(key, _pause=False)

@socketio.on('keyboard_text')
def handle_keyboard_text(data):
    # data: { text: string }
    text = data.get('text')
    if text:
        pyautogui.write(text, interval=0.01, _pause=False)

if __name__ == '__main__':
    # Get local IP and print it so the user knows where to connect from phone
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Backend running at http://{local_ip}:5001")
    socketio.run(app, host='0.0.0.0', port=5001)
