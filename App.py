from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global dictionary to store sensor values
sensor_data = {
    'temperature': 'N/A',
    'humidity': 'N/A'
}

@app.route('/')
def dashboard():
    return render_template('index.html', data=sensor_data)

@app.route('/update', methods=['POST'])
def update():
    content = request.get_json()
    if content and 'temperature' in content and 'humidity' in content:
        sensor_data['temperature'] = content['temperature']
        sensor_data['humidity'] = content['humidity']
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

