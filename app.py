
from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

def get_top_output():
    """Fetches system top command output."""
    try:
        output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
        return "<pre>" + output + "</pre>"
    except Exception as e:
        return f"Error fetching top command output: {str(e)}"

@app.route('/htop')
def htop():
    """Displays system information and top command output."""
    name = "Partheev Reddy Bojja"  # Replace with your actual name
    username = os.getenv('USER', 'Unknown')  # Safer alternative to os.getlogin()

    # Set timezone to IST (Indian Standard Time)
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {server_time}</p>
    <h2>Top Command Output</h2>
    {get_top_output()}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
