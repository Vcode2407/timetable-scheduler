import requests

BASE_URL = 'http://localhost:5000/api/schedule'

def test_create_and_get_schedule():
    payload = {
        'course': 'Test101',
        'day': 'Monday',
        'time': '10:00',
        'location': 'Room A'
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201

    response = requests.get(BASE_URL)
    assert response.status_code == 200
    schedules = response.json()
    assert any(schedule['course'] == 'Test101' for schedule in schedules)

def test_delete_schedule():
    payload = {
        'course': 'Test102',
        'day': 'Tuesday',
        'time': '11:00',
        'location': 'Room B'
    }
    requests.post(BASE_URL, json=payload)
    response = requests.delete(f'{BASE_URL}/Test102')
    assert response.status_code == 200
