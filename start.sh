#!/bin/bash



echo "🚀 Starting Mouse & Keyboard Controller..."

# Function to get local IP
get_local_ip() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        ip=$(ipconfig getifaddr en0)
        [ -z "$ip" ] && ip=$(ipconfig getifaddr en1)
        echo "$ip"
    else
        echo $(hostname -I | awk '{print $1}')
    fi
}

IP=$(get_local_ip)
export ALLOWED_HOST=${ALLOWED_HOST:-"mac.fritz.box"}

if [ -z "$IP" ]; then
    IP="localhost"
    echo "⚠️  Could not detect local IP. Using localhost."
else
    echo "✅ Local IP detected: $IP"
fi

# Start Backend
echo "📦 Starting Backend (Flask)..."
source venv/bin/activate
python3 app.py &
BACKEND_PID=$!

# Wait for backend to be ready
sleep 2

# Start Frontend
echo "🌐 Starting Frontend (Vite)..."
cd frontend
pnpm dev --host --port 5173 &
FRONTEND_PID=$!

echo ""
echo "----------------------------------------------------"
echo "📱 ACCESS ON YOUR PHONE:"
echo "http://$IP:5173"
echo "http://$ALLOWED_HOST:5173"
echo "----------------------------------------------------"
echo ""

# Keep the script running
wait
