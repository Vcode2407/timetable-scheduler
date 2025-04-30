import sqlite3

def init_db():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS schedules
                 (course TEXT, day TEXT, time TEXT, location TEXT)''')
    conn.commit()
    conn.close()

def add_schedule(course, day, time, location):
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute('INSERT INTO schedules (course, day, time, location) VALUES (?, ?, ?, ?)',
              (course, day, time, location))
    conn.commit()
    conn.close()

def get_schedules():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute('SELECT * FROM schedules')
    schedules = [{'course': row[0], 'day': row[1], 'time': row[2], 'location': row[3]}
                 for row in c.fetchall()]
    conn.close()
    return schedules

def delete_schedule(course):
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute('DELETE FROM schedules WHERE course = ?', (course,))
    conn.commit()
    conn.close()
