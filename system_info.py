from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to get system info
def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    memory = psutil.virtual_memory()
    total_memory = memory.total
    available_memory = memory.available
    used_memory = memory.used
    memory_percentage = memory.percent
    
    disk = psutil.disk_usage('/')
    total_disk = disk.total
    used_disk = disk.used
    free_disk = disk.free
    disk_percentage = disk.percent

    return {
        'cpu_usage': cpu_usage,
        'memory': {
            'total_memory': total_memory,
            'used_memory': used_memory,
            'available_memory': available_memory,
            'memory_percentage': memory_percentage,
        },
        'disk': {
            'total_disk': total_disk,
            'used_disk': used_disk,
            'free_disk': free_disk,
            'disk_percentage': disk_percentage,
        }
    }

@app.route('/api/system_info', methods=['GET'])
def system_info():
    return jsonify(get_system_info())

if __name__ == '__main__':
    app.run(debug=True)
    