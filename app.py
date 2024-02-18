import csv
from flask import Flask, request, render_template, redirect
import platform
import socket
import psutil
import secrets
from flask import request

app = Flask(__name__)

# Dictionary to store device information based on token
device_info = {}


def check_for_proxy():
    # Implement logic to check for proxy applications
    # You can check for common proxy ports or known proxy server IPs
    return False  # Placeholder, replace with actual logic


def check_for_remote_desktop():
    # Implement logic to check for remote desktop software
    # You can check for processes associated with remote desktop applications
    for proc in psutil.process_iter(['name']):
        if 'AnyDesk' in proc.info['name'] or 'TeamViewer' in proc.info['name']:
            return True
    return False


def save_client_data_to_csv(token, name, data):
    file_path = 'client_data.csv'
    fieldnames = ['Token', 'Name', 'OS', 'Browser', 'IP Address', 'Hostname', 'Connected Devices', 'Proxy Detected', 'Remote Desktop Detected']
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'Token': token,
            'Name': name,
            'OS': data['os'],
            'Browser': data['browser'],
            'IP Address': data['ip'],
            'Hostname': data['hostname'],
            'Connected Devices': ', '.join(map(str, data['connected_devices'])),
            'Proxy Detected': data['proxy_detected'],
            'Remote Desktop Detected': data['remote_desktop_detected']
        })


@app.route('/', methods=['GET', 'POST'])
def index():
    unique_link = None
    client_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        unique_token = secrets.token_hex(4)
        unique_link = request.url_root + f"check_device?token={unique_token}&name={name}"
        device_info[unique_token] = "Device information will be fetched here"

    # Read client data from CSV file
    with open('client_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        client_data = list(reader)

    return render_template('index.html', unique_link=unique_link, client_data=client_data)


@app.route('/check_device', methods=['GET'])
def check_device():
    token = request.args.get('token')
    name = request.args.get('name')
    if token in device_info:
        os_info = platform.platform()
        
        # Retrieve browser information
        browser_info = request.user_agent.browser if request.user_agent else "Unknown Browser"
        
        ip_address = request.remote_addr
        hostname = socket.gethostname()
        connected_devices = psutil.disk_partitions()
        proxy_detected = check_for_proxy()
        remote_desktop_detected = check_for_remote_desktop()
        data = {
            'os': os_info,
            'browser': browser_info,
            'ip': ip_address,
            'hostname': hostname,
            'connected_devices': connected_devices,
            'proxy_detected': proxy_detected,
            'remote_desktop_detected': remote_desktop_detected
        }
        save_client_data_to_csv(token, name, data)
        print("Browser Info:", browser_info)  # Print browser information for debugging
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        return "Invalid token"



if __name__ == '__main__':
    app.run(debug=True)
