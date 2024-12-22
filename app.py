from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    ssid = request.form['ssid']
    password = request.form['password']
    # Save credentials to wpa_supplicant.conf
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as f:
        f.write(f'\nnetwork={{\n    ssid="{ssid}"\n    psk="{password}"\n}}\n')
    # Restart the network service
    os.system('sudo systemctl restart networking')
    return "Connecting..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
