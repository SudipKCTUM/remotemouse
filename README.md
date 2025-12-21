# Mac Remote Controller 🖱️⌨️

A premium, low-latency remote mouse and keyboard controller for macOS. Control your Mac from your phone through a sleek, mobile-optimized web interface.

## ✨ Features

- **Responsive Touchpad**: Low-latency cursor movement with adjustable sensitivity.
- **Native Keyboard Integration**: Use your phone's native keyboard to type directly into any app on your Mac.
- **System Controls**: Dedicated buttons for Left/Right click, Space, Backspace, and Enter.
- **Modern UI**: Dark-themed, glassmorphic design built with React and Tailwind-inspired CSS.
- **Cross-Platform**: Works on any device with a modern web browser on your local network.

## 🛠 Tech Stack

- **Backend**: Python (Flask-SocketIO), PyAutoGUI (for system-level control).
- **Frontend**: React, TypeScript, Vite, Socket.io-client.
- **Styling**: Vanilla CSS with modern premium aesthetics (Glassmorphism, Outfit font).

## 🚀 Quick Start

### 1. Prerequisites
- macOS (tested on macOS Sequoia/Sonoma)
- Python 3.x
- Node.js & pnpm

### 2. Setup
Clone the repository and run the start script:
```bash
# Clone the repository
cd mouse

# Make the start script executable (if needed)
chmod +x start.sh

# Run the system
./start.sh
```
The script will automatically set up the Python virtual environment (`venv`), install dependencies, and start both the backend and frontend.

### 3. Grant Permissions
macOS requires explicit permissions for apps to control the system.
1. Go to **System Settings > Privacy & Security**.
2. Under **Accessibility**, add/enable your Terminal (e.g., iTerm or Terminal).
3. Under **Input Monitoring**, ensure your Terminal is allowed.

### 4. Connect
Open the URL shown in your terminal on your phone (usually `http://192.168.x.x:5173`).

## ⚙️ Configuration

- **Sensitivity**: Adjust the mouse movement speed via the settings gear icon in the app.
- **Allowed Hosts**: You can configure allowed hostnames (like `mac.fritz.box`) in the `frontend/.env` file or by passing it to the start script:
  ```bash
  ALLOWED_HOST=my-mac.local ./start.sh
  ```

## 📝 License
MIT
