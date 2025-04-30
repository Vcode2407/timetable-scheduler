from flask import Flask, request, jsonify
from database import init_db, add_schedule, get_schedules, delete_schedule

app = Flask(__name__)

@app.route('/api/schedule', methods=['POST'])
def create_schedule():
    data = request.get_json()
    if not all(key in data for key in ['course', 'day', 'time', 'location']):
        return jsonify({'error': 'Missing fields'}), 400
    add_schedule(data['course'], data['day'], data['time'], data['location'])
    return jsonify({'message': 'Schedule added'}), 201

@app.route('/api/schedule', methods=['GET'])
def list_schedules():
    schedules = get_schedules()
    return jsonify(schedules), 200

@app.route('/api/schedule/<course>', methods=['DELETE'])
def remove_schedule(course):
    delete_schedule(course)
    return jsonify({'message': 'Schedule deleted'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
