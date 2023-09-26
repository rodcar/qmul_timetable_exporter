import requests
import json
from ics import Calendar, Event

# dates to exports
date_start = '2023-09-01'
date_end = '2024-12-31'

# QMUL+ timetable endpoint
qmul_timetable_endpoint = f'https://qmul.ombiel.co.uk/campusm/sso/cal2/Course%20Timetable?start={date_start}T23%3A00%3A00.000Z&end={date_end}T23%3A59%3A59.000Z'

# replace with your own QMUL+ cookie after log in (through Chrome Dev Tools)
cookie = ''

response = requests.get(qmul_timetable_endpoint, headers={'Cookie': cookie})

if response.status_code == 200:
    print('Request successful')

    events = json.loads(response.text).get('events', [])
    cal = Calendar()

    for event in events:
        ics_event = Event()
        ics_event.name = event['desc1']
        ics_event.description = event['desc2']
        ics_event.location = event['locAdd1']
        ics_event.begin = event['start']
        ics_event.end = event['end']
        cal.events.add(ics_event)

    with open('qmul_timetable_cal.ics', 'w') as f:
        f.write(str(cal))
else:
    print(f'Request failed with status code: {response.status_code}')