# Magic methods usage strongly recommended!
# 1. Setup Google Calendar APi - https://developers.google.com/calendar/quickstart/python
# 2. Create a simple calender event - https://developers.google.com/calendar/create-events
# 3. Load calendar event from file T2. OOP\Meta class\uz_bukovel_event.json
# 4. Create calendar event (don't forget to remove my email from json file)

import os.path
from googleapiclient.discovery import build

from oauth2client import client
import json
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
ACCESS_TOKEN = ""


class Event(object):
    def __init__(self, summary: str, location: str, description: str, start: str, end: str, recurrence: str,
                 attendees: str, reminders: str):
        self.summary = summary
        self.location = location
        self.description = description
        self.start = start
        self.end = end
        self.recurrence = recurrence
        self.attendees = attendees
        self.reminders = reminders

    def __str__(self) -> str:
        return f"Event: {self.summary}"

    @classmethod
    def from_file(cls, file_path: str) -> "Event":
        with open(file_path, encoding="utf8") as json_file:
            return cls(**json.load(json_file))

    def to_json(self) -> dict:
        return {
            "summary": self.summary,
            "location": self.location,
            "description": self.description,
            "start": self.start,
            "end": self.end,
            "recurrence": self.recurrence,
            "attendees": self.attendees,
            "reminders": self.reminders,
        }


def main() -> None:
    credentials = client.AccessTokenCredentials(
        ACCESS_TOKEN,
        'my-calendar-bot/1.0',
    )
    service = build('calendar', 'v3', credentials=credentials)

    event_bukovel_path = os.path.abspath("../Meta class/uz_bukovel_event.json")
    event_bukovel_obj = Event.from_file(event_bukovel_path)

    event = service.events().insert(calendarId='primary', body=event_bukovel_obj).execute()
    print(F'Event summary: {event.get("summary")}')


if __name__ == '__main__':
    main()
