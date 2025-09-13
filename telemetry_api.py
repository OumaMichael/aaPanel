from flask import Flask, request, jsonify
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

DATABASE = 'telemetry.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            data TEXT NOT NULL
        )''')
        conn.commit()

@app.route('/telemetry', methods=['POST'])
def receive_telemetry():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        timestamp = datetime.now().isoformat()
        data_str = json.dumps(data)

        with get_db() as conn:
            conn.execute('INSERT INTO telemetry (timestamp, data) VALUES (?, ?)', (timestamp, data_str))
            conn.commit()

        return jsonify({'message': 'Telemetry data received and stored'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    try:
        with get_db() as conn:
            cursor = conn.execute('SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 100')
            rows = cursor.fetchall()

        telemetry_data = []
        for row in rows:
            telemetry_data.append({
                'id': row[0],
                'timestamp': row[1],
                'data': json.loads(row[2])
            })

        return jsonify(telemetry_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
